from selenium.common.exceptions import NoSuchElementException
from Find import Find
from WebElement.Waitor import Waitor


class Element(Find):

    def __init__(self):
        self.interval = 0.5
        self.timeout = 20
        Find.__init__(self)

    def _selenium_context(self):
        pass

    def wait_for(self):
        return Waitor(self, self.interval, self.timeout)

    def get_interval(self):
        return self.interval

    def get_timeout(self):
        return self.timeout

    def set_interval(self, interval):
        self.interval = interval

    def set_timeout(self, timeout):
        self.timeout = timeout

    def click(self):
        try:
            self._selenium_context().click()
        except Exception as handleRetry:
            try:
                self.wait_for().visible()
                self._selenium_context().click()
            except Exception as e:
                raise NoSuchElementException

    def send_keys(self, keys):
        try:
            self._selenium_context().send_keys(keys)
        except Exception as handleRetry:
            try:
                self.wait_for().visible()
                self._selenium_context().send_keys(keys)
            except Exception as e:
                raise NoSuchElementException


    def set_value(self, keys):
        try:
            self._selenium_context().set_value(keys)
        except Exception as handleRetry:
            try:
                self.wait_for().visible()
                self._selenium_context().set_value(keys)

            except Exception as e:
                raise NoSuchElementException

    def drag_and_drop(self, origin_el, destination_el):
        pass

    def exist(self):
        try:
            self._refresh()
            return True
        except Exception as handleRetry:
            return False


    def visible(self):
        try:
            return self._selenium_context().is_displayed()
        except Exception as handleRetry:
            try:
                self._refresh()
                return self._selenium_context().is_displayed()
            except Exception as e:
                return False

    def clear(self):
        try:
            self._selenium_context().clear()
        except Exception as handleRetry:
            try:
                self.wait_for().visible()
                self._selenium_context().clear()
            except Exception as e:
                raise NoSuchElementException

    #TODO: We need to wrap more method here.