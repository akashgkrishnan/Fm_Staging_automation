from selenium.webdriver.common.by import By


class EmployerHome:

    new_interview = (By.LINK_TEXT, 'New Interview')

    add_deposit = (By.LINK_TEXT, 'Add Deposit')

    security_deposit = (By.TAG_NAME, 'h5')

    job_profile = (By.XPATH, "//span[contains(text(),'Job Profile')]")

    candidate_profile = (By.XPATH, "//span[contains(text(),'Candidate Profile')]")

    dashboard = (By.XPATH, "//span[contains(text(),'Dashboard')]")



    def __init__(self, driver):
        self.driver = driver

    def get_new_interview(self):
        return self.driver.find_element(*EmployerHome.new_interview)

    def get_add_deposit(self):
        return self.driver.find_element(*EmployerHome.add_deposit)

    def get_security_deposit(self):
        return self.driver.find_element(*EmployerHome.security_deposit)

    def get_job_profile(self):
        return self.driver.find_element(*EmployerHome.job_profile)

    def get_candidate_profile(self):
        return self.driver.find_element(*EmployerHome.candidate_profile)

    def get_dashboard(self):
        return self.driver.find_element(*EmployerHome.dashboard)




