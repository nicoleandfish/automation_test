import pytest
from utils.browser import get_page

@pytest.fixture
def page():
    page, browser, p = get_page()
    yield page
    browser.close()
    p.stop()