from selenium.webdriver.common.by import By


class FmContactPage:

    name = (By.XPATH, '//input[@name = "name"]')
    email = (By.XPATH, '//input[@name = "mail"]')
    phone = (By.XPATH, '//input[@name = "phone"]')
    company = (By.XPATH, '//input[@name = "company"]')
    submit_btn = (By.XPATH, "button[contains(text(), 'Submit')]")

    def __init__(self, driver):
        self.driver = driver

    def get_name_field(self):
        return self.driver.find_element(*FmContactPage.name)

    def get_email_field(self):
        return self.driver.find_element(*FmContactPage.email)

    def get_phone_field(self):
        return self.driver.find_element(*FmContactPage.phone)

    def get_company_field(self):
        return self.driver.find_element(*FmContactPage.company)

    def get_submit_btn(self):
        return self.driver.find_element(*FmContactPage.submit_btn)