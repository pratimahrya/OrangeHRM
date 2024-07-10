from selenium.webdriver.common.by import By
class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_class_name = "oxd-userdropdown-tab"
        self.logout_link_linkText = "Logout"


    def click_welcome(self):
        self.driver.find_element(By.CLASS_NAME, self.welcome_class_name).click()


    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()