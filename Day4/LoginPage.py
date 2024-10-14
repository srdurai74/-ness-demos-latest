from selenium.webdriver.common.by import By

from LPLocators import LPLocators
from DashboardPage import DashboardPage

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.username_loc_by_name = LPLocators.username_loc_by_name
        self.password_loc_by_name = LPLocators.password_loc_by_name
        self.loginbtn_loc_by_xpath = LPLocators.loginbtn_loc_by_xpath

    def enter_username(self,username):
        driver = self.driver
        driver.find_element(By.NAME,self.username_loc_by_name).send_keys(username)

    def enter_password(self, password):
        driver = self.driver
        driver.find_element(By.NAME, self.password_loc_by_name).send_keys(password)

    def click_login(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.loginbtn_loc_by_xpath).click()


    def check_valid_login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return DashboardPage(self.driver)
