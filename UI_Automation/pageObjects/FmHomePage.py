from selenium.webdriver.common.by import By


class FmHomePage:
    employer = (By.XPATH, "//a[contains(text(),'employer')]")
    interviewer = (By.XPATH, "//a[contains(text(),'interviewer')]")
    employer_sign_up = (By.XPATH, "//a[contains(text(),'Employer Sign Up')]")
    employer_sign_in = (By.XPATH, "//a[contains(text(),'Employer Log In')]")
    pricing = (By.XPATH, "//a[contains(text(), 'Pricing')x`]")
    contact = (By.XPATH, "//a[contains(text(),'Contact Us')]")


    def __init__(self, driver):
        self.driver = driver

    def get_employer(self):
        return self.driver.find_element(*FmHomePage.employer)

    def get_interviewer(self):
        return self.driver.find_element(*FmHomePage.interviewer)

    def get_pricing(self):
        return self.driver.find_element(*FmHomePage.pricing)

    def get_contact(self):
        return self.driver.find_element(*FmHomePage.contact)

    def get_employer_signUp(self):
        return self.driver.find_element(*FmHomePage.employer_sign_up)

    def get_employer_sign_in(self):
        return self.driver.find_element(*FmHomePage.employer_sign_in)

