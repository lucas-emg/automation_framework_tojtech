from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def webdriver_factory(browser: str = "Chrome"):

    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--lang=en")
        options.page_load_strategy = "none"
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    else:
        raise Exception("Unsupported browser. Please use 'Chrome'")

    return driver
