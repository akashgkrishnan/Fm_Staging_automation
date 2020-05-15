from selenium.webdriver.common.by import By


class ScheduleInterview:

    select_job_profile = (By.XPATH, '//tr[1]//td[1]//label[1]//span[1]')
    select_interview_type = (By.XPATH, "//label[contains(text(),'Telephonic')]")
    proceed_button = (By.XPATH, "//button[contains(text(),'Proceed')]")
    select_candidate_profile = (By.XPATH, "//span[@class='selectCandidate_checkmark__lqSNt']")
    select_interviewer = (By.XPATH, "//tr[1]//td[2]//label[1]//span[1]")
    availability_button = (By.XPATH, "//tr[1]//td[6]")
    select_first_availability = (By.XPATH, "//span[@class='Availability_checkmark__Xqj5j']")
    next_button = (By.XPATH, "//button[contains(text(),'Next')]")
    availability_ok_button = (By.XPATH, "//button[contains(@class,'Availability_okButton__TZfAW')]")

    def __init__(self, driver):
        self.driver = driver

    def get_select_first_job_profile(self):
        return self.driver.find_element(*ScheduleInterview.select_job_profile)

    def get_get_telephonic_radio_mode(self):
        return self.driver.find_element(*ScheduleInterview.select_interview_type)

    def get_proceed_button(self):
        return self.driver.find_element(*ScheduleInterview.proceed_button)

    def get_select_first_candidate_profile(self):
        return self.driver.find_element(*ScheduleInterview.select_candidate_profile)

    def get_select_first_interviewer(self):
        return self.driver.find_element(*ScheduleInterview.select_interviewer)

    def get_availability_button(self):
        return self.driver.find_element(*ScheduleInterview.availability_button)

    def get_select_first_availability(self):
        return self.driver.find_element(*ScheduleInterview.select_first_availability)

    def get_next_button(self):
        return self.driver.find_element(*ScheduleInterview.next_button)

    def get_confirm_availability_button(self):
        return self.driver.find_element(*ScheduleInterview.availability_ok_button)

