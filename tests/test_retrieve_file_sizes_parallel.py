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

    def _fake_process_single_url(url, product_id, resource_id, cache, ignore_cache, clean_warnings_only, product):
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
