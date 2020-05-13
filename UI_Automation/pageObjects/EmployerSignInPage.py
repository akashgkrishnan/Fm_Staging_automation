from selenium.webdriver.common.by import By


class SignInPage:
    email = (By.XPATH, '//input[@name="email"]')
    password = (By.XPATH, '//*[@id="_password"]')
    login_button = (By.XPATH, '//*[@id="employerForm"]/div[4]/button')

    def __init__(self, driver):
        self.driver = driver

    def get_email_field(self):
        return self.driver.find_element(*SignInPage.email)

    def get_password_field(self):
        return self.driver.find_element(*SignInPage.password)

    def get_login_button(self):
        return self.driver.find_element(*SignInPage.login_button)
