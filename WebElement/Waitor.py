from Utilitys.Utils import Utils


class Waitor:

    def __init__(self, webElement, interval=0.5, timeout=20):
        self.web_element = webElement
        self.interval = interval
        self.timeout = timeout


    def exist(self):
        Utils.wait_for(self.web_element.exist, self.interval, self.timeout)

    def visible(self):
        Utils.wait_for(self.web_element.visible, self.interval, self.timeout)


