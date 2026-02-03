import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_open_google(setup):
    setup.get("https://www.google.com")
    assert "Google" in setup.title

def test_bing_title(setup):
    setup.get("https://www.bing.com")
    assert "Bing" in setup.title