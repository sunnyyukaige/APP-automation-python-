from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilitys.Utils import Utils

__author__ = 'Fox'

class WaitUtils:
    @staticmethod
    def wait_for_exist(driver, by, value, interval=0.5, timeout=20):
        return Utils.wait_until(Utils.try_function(driver.find_element, by=by, value=value), interval=interval, timeout=timeout)

    @staticmethod
    def wait_for_element_present(driver, by, value, interval=0.5, timeout=20):
        return WebDriverWait(driver, timeout, interval).until(EC.presence_of_element_located((by, value)))

    @staticmethod
    def wait_for_element_visible(driver, by, value, interval=0.5, timeout=20):
        return WebDriverWait(driver, timeout, interval).until(EC.visibility_of_element_located((by, value)))

    @staticmethod
    def wait_for_element_clickable(driver, by, value, interval=0.5, timeout=20):
        return WebDriverWait(driver, timeout, interval).until(EC.element_to_be_clickable((by, value)))

    @staticmethod
    def wait_for_not_exist(driver, by, value, interval=500, timeout=20000):
        pass