from selenium.webdriver.common.by import By


class EmployerHome:
    new_interview = (By.CSS_SELECTOR, 'button[class*="scheduleInterviewer_searchButton__1N58S"]')

    def __init__(self, driver):
        self.driver = driver

    def get_new_interview(self):
        return self.driver.find_element(*EmployerHome.new_interview)
