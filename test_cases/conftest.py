import pytest
from selenium import webdriver
# the pytest_addoption function is a hook that allows you to define command
#-line options for a website
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="specify the browser: chrome or firefox or edge")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("browser must be 'chrome' or 'firefox' or 'edge'")
    return driver

    # ensure driver closes after test


