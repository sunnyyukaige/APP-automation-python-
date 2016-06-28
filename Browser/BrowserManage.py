import subprocess
from Browser.Browser import Browser
import os

__author__ = 'sunny.yu2'

class BrowserManage:
    browsers = None
    @staticmethod
    def setBrowser():
        if BrowserManage.browsers==None:
                app=os.path.abspath( os.path.join(os.path.dirname(__file__),
                             '../../build/outputs/apk/app-dev-debug.apk'))
                BrowserManage.browsers = Browser("appium", command_executor='http://127.0.0.1:4723/wd/hub',
                                        desired_capabilities={
                                            'app': app,
                                            'platformName': 'Android',
                                            'platformVersion': '6.0',
                                            'deviceName': 'Google Nexus 6P - 6.0.0 - API 23 - 1440x2560',
                                            'appWaitActivity': 'com.ef.hugin.ui.activities.LoginActivity'
                                        })

        return BrowserManage.browsers

    def clearBrowser(self):
             BrowserManage.browsers=None

    def start_Appium(self, host, port, appium_log_path): #device_uid,
          #appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600
          errormsg = ""
          appium_server_url =""
          try:
                cmd ='appium -a '+ host +' -p '+ str(port)+\
                       ' --session-override --log '\
                     + '"'+appium_log_path + '" --command-timeout 600'
                print (cmd)
                p = subprocess.call(cmd, shell=True,stdout=open('../logs.log','w'),stderr=subprocess.STDOUT)
          except Exception as msg:
              errormsg = str(msg)
          return appium_server_url, errormsg

    def stop_Appium(self):
          errormsg = ""
          try:
                cmd ='taskkill /F /FI "WINDOWTITLE eq stopAppiumServer"'
                print (cmd)
                p = subprocess.call(cmd, shell=True,stdout=open('../logs.log','w'),stderr=subprocess.STDOUT)
          except Exception as msg:
              errormsg = str(msg)
          return  errormsg
