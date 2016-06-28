from selenium import webdriver as SeleniumDriver
from appium import webdriver as AppiumDriver
from selenium.common.exceptions import NoAlertPresentException
from Find import Find
from Utilitys.SeleniumUtils import SeleniumUtils

from Utilitys.Utils import Utils

__author__ = 'karl.gong&fox&sunny'


class BrowserType:
    IE = "ie"
    FIREFOX = "firefox"
    CHROME = "chrome"
    ANDROID = "android"
    OPERA = "opera"
    SAFARI = "safari"
    APPIUM = "appium"


class Browser(Find):
    def __init__(self, browser_type=BrowserType.CHROME, **browser_args):
        Find.__init__(self)
        browser_type_in_lower = browser_type.lower()
        if browser_type_in_lower == "ie":
            self.__browser_type = BrowserType.IE
            self.__web_driver = SeleniumDriver.Ie(**browser_args)
        elif browser_type_in_lower == "firefox" or browser_type_in_lower == "ff":
            self.__browser_type = BrowserType.FIREFOX
            self.__web_driver = SeleniumDriver.Firefox(**browser_args)
        elif browser_type_in_lower == "chrome":
            self.__browser_type = BrowserType.CHROME
            self.__web_driver = SeleniumDriver.Chrome(**browser_args)
        elif browser_type_in_lower == "android":
            self.__browser_type = BrowserType.ANDROID
            self.__web_driver = SeleniumDriver.Android(**browser_args)
        elif browser_type_in_lower == "opera":
            self.__browser_type = BrowserType.OPERA
            self.__web_driver = SeleniumDriver.Opera(**browser_args)
        elif browser_type_in_lower == "safari":
            self.__browser_type = BrowserType.SAFARI
            self.__web_driver = SeleniumDriver.Safari(**browser_args)
        elif browser_type_in_lower == "appium":
            self.__browser_type = BrowserType.APPIUM
            self.__web_driver = AppiumDriver.Remote(**browser_args)
        else:
            raise Exception("The browser type [%s] is not supported." % browser_type)

    def get_browser(self):
        return self

    def _web_driver(self):
        return self.__web_driver

    def _selenium_context(self):
        return self.__web_driver

    def _refresh(self):
        # For the browser, there's no need to refresh.
        pass

    def get_browser_type(self):
        return self.__browser_type

    def before_startup(self, method):
        self.__web_driver.start_client = method

    def after_shutdown(self, method):
        self.__web_driver.stop_client = method

    def start_session(self, desired_capabilities, browser_profile=None):
        self.__web_driver.start_session(desired_capabilities, browser_profile)

    def maximize_window(self):
        self.__web_driver.maximize_window()

    def set_page_load_timeout(self, timeout):
        self.__web_driver.set_page_load_timeout(timeout / 1000.0)

    def set_script_timeout(self, time_to_wait):
        self.__web_driver.set_script_timeout(time_to_wait / 1000.0)

    def set_wait_element_interval(self, interval):
        self.__wait_element_interval = interval

    def get_wait_element_interval(self):
        return self.__wait_element_interval

    def set_wait_element_timeout(self, timeout):
        self.__wait_element_timeout = timeout

    def get_wait_element_timeout(self):
        return self.__wait_element_timeout

    def execute_script(self, script, *args):
        return self.__web_driver.execute_script(script, *args)

    def execute_async_script(self, script, *args):
        return self.__web_driver.execute_async_script(script, *args)

    def open(self, url):
        self.__web_driver.get(url)

    def get_title(self):
        return self.__web_driver.title

    def get_pageSource(self):
        return self.__web_driver.page_source

    def refresh(self):
        self.__web_driver.refresh()

    def back(self):
        self.__web_driver.back()

    def forward(self):
        self.__web_driver.forward()

    def quit(self):
        self.__web_driver.quit()

    def get_current_url(self):
        return self.__web_driver.current_url

    def switch_to_frame(self, frame_reference):
        self.__web_driver.switch_to.frame(frame_reference)

    def switch_to_parent_frame(self):
        self.__web_driver.switch_to.parent_frame()

    def switch_to_default_content(self):
        self.__web_driver.switch_to.default_content()

    def get_alert(self):
        return self.__web_driver.switch_to.alert

    def is_alert_present(self):
        try:
            alert = self.__web_driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    def wait_for_alert_present(self):
        Utils.wait_for(self.is_alert_present)

    def get_cookies(self):
        return self.__web_driver.get_cookies()

    def get_cookie(self, name):
        return self.__web_driver.get_cookie(name)

    def delete_cookie(self, name):
        self.__web_driver.delete_cookie(name)

    def delete_all_cookies(self):
        self.__web_driver.delete_all_cookies()

    def add_cookie(self, cookie_dict):
        self.__web_driver.add_cookie(cookie_dict)

    def get_desired_capabilities(self):
        return self.__web_driver.desired_capabilities

    def get_screenshot_as_file(self, filename):
        return self.__web_driver.get_screenshot_as_file(filename)

    def get_screenshot_as_png(self):
        return self.__web_driver.get_screenshot_as_png()

    def get_screenshot_as_base64(self):
        return self.__web_driver.get_screenshot_as_base64()

    save_screenshot = get_screenshot_as_file

    def get_current_window_handle(self):
        return self.__web_driver.current_window_handle

    def get_window_handles(self):
        return self.__web_driver.window_handles

    def switch_to_window(self, window_reference):
        self.__web_driver.switch_to.window(window_reference)

    def close_window(self, window_reference="current"):
        if window_reference == "current":
            self.__web_driver.close()
        else:
            current_window = self.get_current_window_handle()
            self.switch_to_window(window_reference)
            self.__web_driver.close()
            self.switch_to_window(current_window)

    def set_window_size(self, width, height, window_reference="current"):
        self.__web_driver.set_window_size(width, height, window_reference)

    def get_window_size(self, window_reference="current"):
        return self.__web_driver.get_window_size(window_reference)

    def set_window_position(self, x, y, window_reference="current"):
        self.__web_driver.set_window_position(x, y, window_reference)

    def get_window_position(self, window_reference="current"):
        return self.__web_driver.get_window_position(window_reference)

    def get_orientation(self):
        return self.__web_driver.orientation

    def set_orientation(self, value):
        self.__web_driver = value

    def get_application_cache(self):
        return self.__web_driver.application_cache

    def get_log_types(self):
        return self.__web_driver.log_types

    def get_log(self, log_type):
        return self.__web_driver.get_log(log_type)

    def switch_to_context(self, name):
        self.__web_driver._switch_to.context(name)
        return self._selenium_context().current_context

    def hide_keyboard(self):
        self.__web_driver.find_element_by_xpath("//UIAButton[@name='Hide keyboard']").click()

    def scroll_to(self, element):
        SeleniumUtils.scroll_to(self._selenium_context(), element)

    def scroll_down(self):
        #SeleniumUtils.scroll_to_direction(self._selenium_context(), "Down")

        self._web_driver().swipe(0,0,768,1184)

    def close_App(self):
        self._web_driver().close_app()
        self._web_driver().quit()

    def __str__(self):
        return "Browser [WebDriver: %s][SessionId: %s]" % (self.__web_driver.name, self.__web_driver.session_id)
