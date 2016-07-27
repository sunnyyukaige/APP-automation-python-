import unittest
#import Case.TestLoginCase
#import Case.TestGotoLeads
#import Case.TestLoginManager
#import Case.TestSubmitLeads
import Browser.BrowserManage

browserManager=Browser.BrowserManage.BrowserManage()
'''suite=unittest.TestLoader().loadTestsFromModule(Case.TestLoginCase)
unittest.TextTestRunner().run(suite)
suite=unittest.TestLoader().loadTestsFromModule(Case.TestLoginManager)
unittest.TextTestRunner().run(suite)'''
#browserManager.start_Appium('127.0.0.1','4723','F:/appiumlogsunny.txt')
suite=unittest.TestLoader().discover('Case',pattern='TestSubmitLeadsIOS.py')
unittest.TextTestRunner().run(suite)
#browserManager.stop_Appium()