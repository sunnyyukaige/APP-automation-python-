import os
import subprocess
import time
import signal
from .Utils import Utils


class SeleniumUtils(object):
    @staticmethod
    def scroll_to(driver, element):
        driver.execute_script("mobile: scrollTo", {"element": element.id})

    @staticmethod
    def scroll_to_direction(driver, direction):
        scrollObject = {}
        scrollObject["direction"] = direction
        driver.execute_script("mobile: scrollTo", scrollObject)
    @staticmethod
    def is_port_available(server_ip, port, local_interval=2, local_timeout=10):
        """
        Use telnet command to check the service status. If it's connected, the telnet will not return response.
        :param server_ip: Server ip address
        :param port: Server port
        :param local_interval: After connected, will check the status by this interval
        :param local_timeout: After connected, will disconnect it in timeout.
        :return: True or False
        """
        process = subprocess.Popen('telnet ' + str(server_ip) + " " + str(port), shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        # poll() is the status of the thread, if it's None, means, it's running.
        while process.poll() is None:
            time.sleep(local_interval)
            if local_timeout - local_interval <= 0:
                os.kill(process.pid, signal.SIGKILL)
                os.waitpid(-1, os.WNOHANG)
                return True
            local_timeout = local_timeout - local_interval
        output = process.stdout.readlines()
        list_result = [x for x in output if "Connected" in str(x)]
        if len(list_result) == 0:
            return False
        else:
            return True

    @staticmethod
    def is_service_available(server_ip, port, interval, timeout):
        return Utils.wait_for(SeleniumUtils.is_port_available, interval=interval, timeout=timeout, server_ip=server_ip,
                              port=port)
