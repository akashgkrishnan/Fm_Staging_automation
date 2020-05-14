from selenium.webdriver.common.by import By


class EmployerJobProfile:

    create_profile = (By.XPATH, "//button[@class='btn btn-warning']")

    job_title_field = (By.XPATH, '//input[@name="jobTitle"]')

    client_name_field = (By.XPATH, '//input[@name="clientname"]')

    min_exp_down = (By.CLASS_NAME, "css-9ia8u")

    min_exp_field = (By.XPATH, '//select[@id = "react-select-5-option-1"]')


    max_exp_down = (By.CLASS_NAME, ' css-tlfecz-indicatorContainer')

    max_exp =  (By.XPATH, "//input[@id='react-select-3-input']")

    skills_field = (By.XPATH, "//div[@class='css-1d3apon']//div//input")

    submit_job_profile = (By.XPATH, "//button[@class='createJobProfile_Button_2__3OmsW btn btn-warning']")



    def __init__(self, driver):
        self.driver = driver


    def get_create_job_profile(self):
        return self.driver.find_element(*EmployerJobProfile.create_profile)


    def get_job_title_field(self):
        return self.driver.find_element(*EmployerJobProfile.job_title_field)

    def get_client_name_field(self):
        return self.driver.find_element(*EmployerJobProfile.client_name_field)

    def get_min_exp_down(self):
        return self.driver.find_element(*EmployerJobProfile.min_exp_down)

    def get_min_exp_field(self):
        return self.driver.find_element(*EmployerJobProfile.min_exp_field)

    def get_max_exp_down(self):
        return self.driver.find_element(*EmployerJobProfile.max_exp_down)

    def get_max_exp_field(self):
        return

    def get_skills_field(self):
        return self.driver.find_element(*EmployerJobProfile.skills_field)

    def get_submit_job_profile(self):
        return self.driver.find_element(*EmployerJobProfile.submit_job_profile)