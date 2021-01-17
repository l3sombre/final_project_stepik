import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

def pytest_addoption(parser):
    parser.addoption('--language', action="store", default="en", help="Choose a language of your tests: ")
   

@pytest.fixture(scope="function")
def browser(request):
    test_language = request.config.getoption("language")
    if (test_language):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages':test_language})
        browser = webdriver.Chrome(options=options)
    else:
        print ("Please, choose a language of the site. You have to add parameter '--language lang_code' before starting a test.")
    yield browser
    time.sleep(3)
    browser.quit()

