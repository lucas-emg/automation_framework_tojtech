from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def webdriver_factory(browser: str = "Chrome"):
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en")
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.page_load_strategy = "none"
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options
        )
    else:
        raise Exception("Unsupported Browser. Please use 'Chrome' or 'Firefox'")

    return driver
