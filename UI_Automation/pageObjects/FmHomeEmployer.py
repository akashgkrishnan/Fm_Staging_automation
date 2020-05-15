from selenium.webdriver.common.by import By


class FmEmployerPage:

    request_demo = (By.XPATH, '//button[contains(text(), "Request Demo")]')
    name = (By.XPATH, '//input[@name="name"]')
    email = (By.XPATH, '//input[@name="mail"]')
    phone = (By.XPATH, '//input[@name="phone"]')
    company = (By.XPATH, '//input[@name="company"]')
    company_wesite = (By.XPATH, '//input[@name="website"]')
    submit_demo = (By.XPATH, '//button[contains(text(), "Submit")]')
    demo_success = (By.XPATH, "//div[@id='contact-form-success']//div[@class='submit_message']")


    def __init__(self, driver):
        self.driver = driver

    def get_request_demo(self):
        return self.driver.find_element(*FmEmployerPage.request_demo)

    def get_name_field(self):
        return self.driver.find_element(*FmEmployerPage.name)

    def get_email_field(self):
        return self.driver.find_element(*FmEmployerPage.email)

    def get_phone_field(self):
        return self.driver.find_element(*FmEmployerPage.phone)

    def get_company_field(self):
        return self.driver.find_element(*FmEmployerPage.company)

    def get_company_website_field(self):
        return self.driver.find_element(*FmEmployerPage.company_wesite)

    def get_submit_demo(self):
        return self.driver.find_element(*FmEmployerPage.submit_demo)

    def get_demo_success(self):
        return self.driver.find_element(*FmEmployerPage.demo_success)

