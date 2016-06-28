__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By


class HomePage(BasePage):

  # def __init__(self):
  #     super(self).__init__()

    def SelectMarketingPlace(self):

        self.browser.set_wait_element_timeout(600000)
        self.browser.find_element(By.ID,'com.ef.hugin.dev:id/home_marketing_place').click()
        self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/select_dialog_list_item_text').click()

    def AddLead(self):
        self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/home_add_lead').click()
        self.browser.get_screenshot_as_file("f:\\sunnytestit.png")

    def LeadsNumber(self):
        return self.browser.find_element(By.ID,'com.ef.hugin.dev:id/dashboard_total').text