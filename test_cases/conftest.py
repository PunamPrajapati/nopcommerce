import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome or firefox or edge")

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
        raise ValueError("Unsupported browser")
    return driver

#hooks for adding environment info in html report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = "Ecommerce Project"
    config.stash[metadata_key]['Test Module Name'] = "Admin Login Test"
    config.stash[metadata_key]['Tester Name'] = "Punam"

#hooks for modifying or deleting environment info in html reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

