import pytest
import time
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(8)
    yield browser
    time.sleep(2)
    browser.quit()
