from selenium.webdriver.common.by import By


class EmployerCandidate:

    create_candidate = (By.XPATH, "//button[contains(text(),'Create')]")
    candidate_name = (By.XPATH, "//input[@name='full_name']")
    candidate_phone = (By.XPATH, "//input[@name='phone_number']")
    candidate_email = (By.XPATH, "//input[@name='mail']")
    upload_resume = (By.XPATH, "//input[@id='upload']")

    def __init__(self, driver):
        self.driver = driver

    def get_create_candidate(self):
        return self.driver.find_element(*EmployerCandidate.create_candidate)

    def get_candidate_name_field(self):
        return self.driver.find_element(*EmployerCandidate.candidate_name)

    def get_exp_field(self):
        return self.driver.find_element()

    def get_candidate_phone_field(self):
        return self.driver.find_element(*EmployerCandidate.candidate_phone)

    def get_candidate_mail(self):
        return self.driver.find_element(*EmployerCandidate.candidate_email)

    def get_upload_resume(self):
        return self.driver.find_element(*EmployerCandidate.upload_resume)



