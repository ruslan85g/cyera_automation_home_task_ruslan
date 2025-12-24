# Automation QA Home Task - Cyera

Automated testing suite for the Demoblaze e-commerce platform and a mock backend API. Built with **Python**, **Pytest**, and **Playwright**.

## Project Overview
- **UI Testing**: Implemented using the Page Object Model (POM) for high maintainability.
- **API Testing**: Validated using `monkeypatch` to mock backend responses for products and cart management.
- **Performance**: Includes a baseline performance check for homepage loading speed.

## Prerequisites
- Python 3.8 or higher
- [Playwright for Python](https://playwright.dev/python/docs/intro)

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
## Execution Modes
To run tests and see the browser window (Headed mode):
```bash
pytest --headed
```

Run only UI Tests::
```bash
pytest tests/ui/ --headed
```

Run only API Tests::
```bash
pytest tests/api/
```


## Project Structure
```text
/pages
  - home_page.py        # POM implementation for site interactions
/tests
  /ui
    - test_products.py    # UI scenarios (Catalog, Navigation, Add to Cart)
    - test_performance.py # Bonus performance metrics
  /api
    - test_mock_api.py    # Complete API workflow (GET/POST/GET)
    - test_negative.py    # Edge cases and error handling responses
requirements.txt          # Project dependencies
conftest.py               # Shared fixtures (base_url) and global configurations