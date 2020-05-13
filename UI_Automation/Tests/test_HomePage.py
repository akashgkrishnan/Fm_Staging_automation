from UI_Automation.pageObjects.EmployerSignUp import EmployerSignUp
from UI_Automation.pageObjects.FmHomePage import FmHomePage
from UI_Automation.utilities.BaseClass import BaseClass
from time import sleep

class TestFmHomePage(BaseClass):
    # def test_employer_landing(self):
    #     home_page = FmHomePage(self.driver)
    #     home_page.get_employer().click()
    #     sleep(3)

    # def test_interviewer_landing(self):
    #     home_page = FmHomePage(self.driver)
    #     home_page.get_interviewer().click()
    #     sleep(3)

    def test_employer_signUp(self):
        home_page = FmHomePage(self.driver)
        home_page.get_employer_signUp().click()
        sleep(5)
        child_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window)
        employee_page = EmployerSignUp(self.driver)
        employee_page.get_company().send_keys('Automation Company 123')
        employee_page.get_fullName().send_keys('Akash G Krishnan')
        employee_page.get_email().click()
        employee_page.get_email().send_keys('akash.krishnan21@mailinator.com')
        employee_page.get_password().send_keys('Testing@123')
        employee_page.get_confirm_password().send_keys('Testing@123')
        employee_page.get_signup_button().click()
        sleep(5)


    # def test_employer_signIn(self):
    #     pass