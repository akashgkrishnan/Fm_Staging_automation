from selenium.webdriver.common.by import By


class FmHomePage:
    employer = (By.XPATH, "//a[contains(text(),'employer')]")
    interviewer = (By.XPATH, '/html/body/header/div/div[2]/ul/li[2]/a')
    employer_sign_up = (By.XPATH, '/html/body/header/div/div[2]/ul/li[6]/a')
    employer_sign_in = (By.XPATH, '/html/body/header/div/div[2]/ul/li[5]/a')

    def __init__(self, driver):
        self.driver = driver

    def get_employer(self):
        return self.driver.find_element(*FmHomePage.employer)

    def get_interviewer(self):
        return self.driver.find_element(*FmHomePage.interviewer)

    def get_employer_signUp(self):
        return self.driver.find_element(*FmHomePage.employer_sign_up)

    def get_employer_sign_in(self):
        return self.driver.find_element(*FmHomePage.employer_sign_in)

