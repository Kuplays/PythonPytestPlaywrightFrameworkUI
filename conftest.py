import os
import sys
import platform

import allure
import pytest
from playwright.sync_api import sync_playwright
from page_objects.login_page import LoginPage
from constants import BASE_URL, DEFAULT_USER_NAME, DEFAULT_USER_PASSWORD

"""
pytest_addoption is used to add various custom command line arguments. In this example we retrieve data from constants
since this data is not secure by default. Otherwise store data in safe non-public place.
"""
def pytest_addoption(parser):
    parser.addoption("--basic_url", action="store", default=BASE_URL)
    parser.addoption("--default_user_name", action="store", default=DEFAULT_USER_NAME)
    parser.addoption("--default_user_password", action="store", default=DEFAULT_USER_PASSWORD)

"""
Browser page fixture. When called it creates an instance of a browser page. We retrieve browser name and headless mode
passed in command line arguments at the start. After yield statements - test is over, and we need to clear the
resources via context and browser closing. Note to self: playwright pytest already defined browser page fixture. It is
for demonstrating purpose only.
"""
@pytest.fixture(scope="function")
def browser_and_page_tuple(request):
    browser_title = request.config.getoption("--browser")
    if isinstance(browser_title, list):
        browser_title = browser_title[0]
    headless_mode = not request.config.getoption("--headed")

    with sync_playwright() as sync_p:
        browser = getattr(sync_p, browser_title).launch(headless=headless_mode)
        ctx = browser.new_context()
        page = ctx.new_page()
        yield page, browser
        ctx.close()
        browser.close()

@pytest.fixture(scope="function")
def browser_page(browser_and_page_tuple):
    browser_page, _ = browser_and_page_tuple
    return browser_page

"""
Session fixture to retrieve basic url. Used to construct either base url or more complex page routes, for example:
basic_url + / + other_resource_path
"""
@pytest.fixture(scope="session")
def basic_url(request):
    return request.config.getoption("--basic_url")

"""
Fixture to retrieve already logged in page to reuse in other tests. Used to get past login screen. The way it works:
we open browser, put default login data and return page with this context.
"""
@pytest.fixture(scope="function")
def get_logged_page(browser_page, basic_url):
    login_page = LoginPage(browser_page, basic_url)
    login_page.go_to()
    login_page.login(DEFAULT_USER_NAME, DEFAULT_USER_PASSWORD)

    return browser_page

"""
Fixture to return basic user credentials as a key-value pair: username and password.
"""
@pytest.fixture(scope="function")
def user_details(request):
    return {"username": request.config.getoption("--default_user_name"),
            "password": request.config.getoption("--default_user_password")
    }

"""
Fixture is autouseable to save screenshot at teardown state
"""
@pytest.fixture(autouse=True)
def make_screenshot_after_test(request, browser_page):
    yield
    allure.attach(
        browser_page.screenshot(),
        name=f"test_{request.node.name}",
        attachment_type=allure.attachment_type.PNG
    )

"""
Fixture to get and write environment information for Allure Environment section
"""
@pytest.fixture(autouse=True)
def add_allure_env(browser_and_page_tuple, browser_name, pytestconfig):
    page, browser = browser_and_page_tuple
    os_name = platform.system()
    os_release = platform.release()
    os_ver = platform.version()
    res_dir = pytestconfig.getoption("--alluredir")
    os.makedirs(res_dir, exist_ok=True)
    env = os.path.join(res_dir, "environment.properties")
    with open(env, "w") as env_file:
        env_file.write(f"Browser={browser_name}\n")
        env_file.write(f"Browser.Version={browser.version}\n")
        env_file.write(f"OS={os_name} {os_release} {os_ver}\n")
        env_file.write(f"Python={sys.version}")