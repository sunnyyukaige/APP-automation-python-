from ..WebElement.Element import Element
from ..WebElement.Waitor import Waitor


class StaticElement(Element):

    def __init__(self, parent, by, value):
        Element.__init__(self)
        self.current_element = None
        self.parent = parent
        self.by = by
        self.value = value

    def _selenium_context(self):
        if not self.current_element:
            self._refresh()
        return self.current_element



    def _refresh(self):
        print("We are refreshed.")
        self.current_element = self.parent.find_element(self.by, self.value)



