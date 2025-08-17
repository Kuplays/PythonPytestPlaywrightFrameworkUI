import pytest
from page_objects.login_page import LoginPage

@pytest.mark.smoke
def test_login_success(browser_page, basic_url, user_details):
    login_page = LoginPage(browser_page, basic_url)
    login_page.go_to()
    login_page.login(user_details.get("username"), user_details.get("password"))

    assert "inventory.html" in browser_page.url