import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():

    service = Service(
        ChromeDriverManager(driver_version="150.0.7871.129").install()
    )

    driver = webdriver.Chrome(service=service)

    yield driver

    driver.quit()


@pytest.fixture
def base_url():
    return "https://www.testmuai.com/selenium-playground/"