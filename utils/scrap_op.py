import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions

from bs4 import BeautifulSoup
from loguru import logger


def init_driver():
    firefox_profile_path = "5vsetjwm.driver"
    driver_profile = webdriver.FirefoxProfile(firefox_profile_path)
    driver = webdriver.Firefox(driver_profile)
    driver.wait = WebDriverWait(driver, 5)
    return driver


def get_soup_from_url(driver, url):
    driver.wait = WebDriverWait(driver, 5)
    try:
        driver.get(url)
    except exceptions.TimeoutException:
        logger.warning("Get Soup Code TimeoutException for %s" % url)
        return False

    try:
        soup = BeautifulSoup(driver.page_source, "html.parser")
    except exceptions.UnexpectedAlertPresentException:
        logger.warning("Make Soup UnexpectedAlertPresentException for %s" % url)
        return ""
    except exceptions.NoSuchWindowException:
        logger.warning("Make Soup NoSuchWindowException for %s" % url)
        return ""

    return soup.prettify()


def get_soup_code_from_file(file):
    try:
        with open(file, "r", encoding="UTF-8") as file:
            file_content = file.read()
        return BeautifulSoup(file_content, "html.parser")
    except FileNotFoundError:
        logger.warning("get_soup_code_from_file : FileNotFoundError for %s" % str(file))
        pass


def save_soup_to_file(soup, file):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="UTF-8") as file:
        file.write(soup)
    return True


def close_driver(driver):
    driver.quit()
    return True
