import time

from selenium.webdriver.common.by import By

from DPLocators import DPLocators


class DashboardPage:

    def __init__(self,driver):
        self.driver = driver
        self.dashbaordmsg_loc_by_xpath = DPLocators.dashbaordmsg_loc_by_xpath


    def get_dashboard_msg(self):
        driver = self.driver

        time.sleep(3)
        msg_element = driver.find_element(By.XPATH,self.dashbaordmsg_loc_by_xpath)
        return msg_element.text


