__author__ = 'sunny.yu2'
from Case.BaseCase import BaseCase
from PageModel.HomePage import HomePage
from PageModel.LoginPage import LoginPage

class SelectMarketing(BaseCase):

    def testRun(self):
        loginPage=LoginPage()
        loginPage.Login('sunny','29394')
        self.homePage=HomePage()
        self.homePage.SelectMarketingPlace()
        self.homePage.AddLead()
