__author__ = 'sunny.yu2'
from PageModel.HomePage import HomePage
from PageModel.LeadPage import LeadPage
from PageModel.LoginPage import LoginPage
from Case.BaseCase import BaseCase

class Submit(BaseCase):

    def testRun(self):
        loginPage=LoginPage()
        loginPage.Login('sunny','29394')
        self.homePage=HomePage()
        self.homePage.SelectMarketingPlace()
        self.homePage.AddLead()
        self.leadPage=LeadPage()
        self.leadPage.StudentName('APPautomation')
        self.leadPage.StudentAge('10')
        self.leadPage.PhoneNumber('13671556095')
        self.leadPage.Scroll_down()
        self.leadPage.Submit()
        self.leadPage.Alert()
        self.assertEqual(self.homePage.LeadsNumber(),"1")


