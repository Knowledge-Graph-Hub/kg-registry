# Test Fixtures for FTP URL Checker

This directory contains test fixture files used by the FTP URL checker tests.

## Files

### test_ftp_resources.yml
Test data for `util/processor.py` check_urls functionality.
- Uses `resource_purl` field (as expected by processor.py)
- Contains examples of FTP files, FTP directories, and HTTPS URLs
- Used for testing URL validation in the processor

### test_ftp_parallel.yml
Test data for `util/retrieve-file-sizes-parallel.py` functionality.
- Uses `product_url` field (as expected by retrieve-file-sizes scripts)
- Contains examples of FTP files, FTP directories, and HTTPS URLs
- Used for testing parallel file size retrieval

## FTP URLs Used

Both fixtures use public FTP servers for testing:
- **FTP File**: `ftp://ftp.ncbi.nlm.nih.gov/README.ftp` - A small text file for testing file size retrieval
- **FTP Directory**: `ftp://ftp.ncbi.nlm.nih.gov/pub/` - A public directory for testing directory detection

## Usage

These fixtures are referenced in `tests/test_ftp_url_checker.py`:
- `TestFTPFixtures` class validates fixture structure and content
- Integration tests can load these fixtures to test end-to-end functionality

Example:
```python
from pathlib import Path
import yaml

FIXTURES_DIR = Path(__file__).parent / "fixtures"

with open(FIXTURES_DIR / "test_ftp_resources.yml", 'r') as f:
    test_data = yaml.safe_load(f)
```
