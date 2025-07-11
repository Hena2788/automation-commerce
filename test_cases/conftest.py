import pytest
from pytest_metadata.plugin import metadata, metadata_key
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
    #return driver
    yield driver
    driver.quit()

    # ensure driver closes after test
#Excluding Custom Parameters from pytest HTML Reports
#hook for delete/modify environment infor in html report
def pytest_configure(config):
    config.stash[metadata_key] ['project Name'] = "Ecommerce project, nopCommerce"
    config.stash[metadata_key] ['Test Module Name'] = "Admin Login Tests"
    config.stash[metadata_key] ['Tester Name'] = "Henok fikadu"
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('plugins', None)

