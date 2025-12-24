import pytest

@pytest.fixture
def ui_url():
    """URL for UI tests"""
    return "https://www.demoblaze.com"

@pytest.fixture
def api_url():
    """Base URL for API mocking"""
    return "https://api.demoblaze.com"