"""Test in-run URL deduplication for parallel file-size retrieval."""


def test_normalize_url_for_lookup_converts_github_blob(retrieve_file_sizes_parallel_module):
    normalized = retrieve_file_sizes_parallel_module.normalize_url_for_lookup(
        "https://github.com/user/repo/blob/main/path/file.txt"
    )

    assert normalized == "https://raw.githubusercontent.com/user/repo/main/path/file.txt"


def test_update_product_file_sizes_deduplicates_shared_urls(
    retrieve_file_sizes_parallel_module,
    monkeypatch,
):
    calls = []

    def _fake_process_single_url(
        url, product_id, resource_id, cache, ignore_cache, clean_warnings_only, product
    ):
        calls.append((url, product_id, resource_id))
        return {
            "url": url,
            "product_id": product_id,
            "resource_id": resource_id,
            "file_size": 123,
            "error_message": None,
            "info": {"content_length": 123},
            "warnings_cleared": 0,
            "should_update": True,
        }

    monkeypatch.setattr(
        retrieve_file_sizes_parallel_module,
        "process_single_url",
        _fake_process_single_url,
    )

    data = {
        "resources": [
            {
                "id": "res1",
                "products": [
                    {
                        "id": "res1.download",
                        "category": "Download",
                        "product_url": "https://example.org/shared.bin",
                    }
                ],
            },
            {
                "id": "res2",
                "products": [
                    {
                        "id": "res2.download",
                        "category": "Download",
                        "product_url": "https://example.org/shared.bin",
                    }
                ],
            },
        ]
    }

    updated_data, updated_products = retrieve_file_sizes_parallel_module.update_product_file_sizes(
        data,
        cache={},
        ignore_cache=False,
        clean_warnings_only=False,
        max_workers=2,
    )

    assert calls == [("https://example.org/shared.bin", "res1.download", "res1")]
    assert updated_data["resources"][0]["products"][0]["product_file_size"] == 123
    assert updated_data["resources"][1]["products"][0]["product_file_size"] == 123
    assert updated_products["res1"][0]["product_file_size"] == 123
    assert updated_products["res2"][0]["product_file_size"] == 123


class _HeaderOnlyResponse:
    """Minimal response stub: a successful reply with controllable headers."""

    def __init__(self, headers, status_code=200):
        self.headers = headers
        self.status_code = status_code
        self.url = "https://example.org/file.bin"

    def close(self):
        pass


def _fake_head(module, monkeypatch, response):
    class _FakeRequests:
        exceptions = module.requests.exceptions

        @staticmethod
        def head(url, **kwargs):
            return response

        @staticmethod
        def get(url, **kwargs):
            return response

    monkeypatch.setattr(module, "requests", _FakeRequests)


def test_missing_content_length_is_not_a_retrieval_error(
    retrieve_file_sizes_parallel_module, monkeypatch
):
    """A reachable URL with no Content-Length must not produce a warning.

    Chunked or dynamically generated responses omit the header. Recording that
    as an error is what put "File was not able to be retrieved" warnings on
    products whose URLs were fine (e.g. edrr-invasive-catalog.dataset).
    """
    mod = retrieve_file_sizes_parallel_module
    _fake_head(mod, monkeypatch, _HeaderOnlyResponse({"Content-Type": "application/octet-stream"}))

    size, error, info = mod.get_file_size_from_header("https://example.org/file.bin")

    assert size is None
    assert error is None, "reachable-but-unmeasurable must not be reported as an error"
    assert info.get("error") is None
    assert info.get("skip_reason") == "no_content_length"


def test_unparseable_content_length_is_not_a_retrieval_error(
    retrieve_file_sizes_parallel_module, monkeypatch
):
    mod = retrieve_file_sizes_parallel_module
    _fake_head(
        mod,
        monkeypatch,
        _HeaderOnlyResponse({"Content-Type": "application/octet-stream", "Content-Length": "many"}),
    )

    size, error, info = mod.get_file_size_from_header("https://example.org/file.bin")

    assert size is None
    assert error is None
    assert info.get("skip_reason") == "no_content_length"


def test_valid_content_length_still_returns_size(retrieve_file_sizes_parallel_module, monkeypatch):
    mod = retrieve_file_sizes_parallel_module
    _fake_head(
        mod,
        monkeypatch,
        _HeaderOnlyResponse({"Content-Type": "application/octet-stream", "Content-Length": "4096"}),
    )

    size, error, info = mod.get_file_size_from_header("https://example.org/file.bin")

    assert size == 4096
    assert error is None


def test_no_content_length_skip_reason_is_honoured_by_cache(
    retrieve_file_sizes_parallel_module,
):
    """The new skip reason must suppress re-checking on later runs."""
    mod = retrieve_file_sizes_parallel_module
    cache = {"https://example.org/file.bin": {"skip_reason": "no_content_length"}}
    should_skip, _ = mod.cache_should_skip("https://example.org/file.bin", cache)
    assert should_skip is True
