from time import sleep
from Utilitys.Utils import Utils
from Utilitys.WaitUtils import WaitUtils


class Find:
    def __init__(self):
        pass

    def get_browser(self):
        pass

    def _selenium_context(self):
        pass

    def _refresh(self):
        pass

    def find_element(self, by, value):
        try:
            try:
                return self._selenium_context().find_element(by, value)
            except Exception as handleRetry:
                self._refresh()
                WaitUtils.wait_for_element_present(self._selenium_context(), by, value)
                return self._selenium_context().find_element(by, value)
        except Exception as e:
            raise Exception("Cannot find element by [%s] under:\n%s\n" % (value, self))

    def find_web_element(self, by, value):
        from .WebElement.StaticElement import StaticElement
        try:
            try:
                self._selenium_context().find_element(by, value)
                return StaticElement(self, by, value)
            except Exception as handleRetry:
                self._refresh()
                element = StaticElement(self, by, value)
                element.wait_for().exist()
                return element
        except Exception as e:
            raise Exception("Cannot find element by [%s] under:\n%s\n" % (value, self))


    def _find_web_element(self, by, value):
        '''
        Find web element, there's no intelligent wait here.
        :param by: By
        :param value: The value of different type selector
        :return:Web element which is found.
        '''
        from .WebElement.StaticElement import StaticElement
        try:
            try:
                self._selenium_context().find_element(by, value)
                return StaticElement(self, by, value)
            except Exception as handleRetry:
                self._refresh()
                self._selenium_context().find_element(by, value)
                return StaticElement(self, by, value)
        except Exception as e:
            raise Exception("Cannot find element by [%s] under:\n%s\n" % (value, self))


    def _find_web_elements(self, by, value, identifier=None):
        from .WebElement.DynamicElement import DynamicElement
        try:
            web_elements = self._selenium_context().find_elements(by, value)
            print("The first find elements number is " + str(web_elements))
        except Exception as handleRetry:
            self._refresh()
            WaitUtils.wait_for_element_present(self._selenium_context(), by, value)
            web_elements = self._selenium_context().find_elements(by, value)
            print("The second find elements number is " + str(web_elements))

        elements = []
        for web_element in web_elements:
            elements.append(DynamicElement(self, web_element, identifier))
        return elements

    def find_web_elements(self, by, value, identifier=None, timeout=20, until_number = 0):
        time = 0
        length = len(self._find_web_elements(by, value, identifier))
        while(length <= until_number):
            length = len(self._find_web_elements(by, value, identifier))
            sleep(0.5)
            time = time + 0.5
            if(time == timeout):
                return False

        return self._find_web_elements(by, value, identifier)

    def find_elements(self, by, value):
        try:
            try:
                return self._selenium_context().find_elements(by, value)
            except Exception as handleRetry:
                self._refresh()
                WaitUtils.wait_for_element_present(self._selenium_context(), by, value)
                return self._selenium_context().find_elements(by, value)
        except Exception as e:
            raise Exception("Cannot find element by [%s] under:\n%s\n" % (value, self))