from UI_Automation.pageObjects.EmployerHome import EmployerHome
from UI_Automation.pageObjects.EmployerSignUp import EmployerSignUp
from UI_Automation.pageObjects.FmHomePage import FmHomePage
from UI_Automation.pageObjects.EmployerSignInPage import SignInPage
from UI_Automation.utilities.BaseClass import BaseClass
from time import sleep

class TestFmHomePage(BaseClass):
    # def test_employer_landing(self):
    #     home_page = FmHomePage(self.driver)
    #     home_page.get_employer().click()
    #     sleep(3)
    #
    # def test_interviewer_landing(self):
    #     home_page = FmHomePage(self.driver)
    #     home_page.get_interviewer().click()
    #     sleep(3)


    # def test_employer_signUp(self):
    #     home_page = FmHomePage(self.driver)
    #     home_page.get_employer_signUp().click()
    #     sleep(5)
    #     child_window = self.driver.window_handles[-1]
    #     self.driver.close()
    #     self.driver.switch_to.window(child_window)
    #     employee_page = EmployerSignUp(self.driver)
    #     employee_page.get_company().send_keys('Automation Company 123')
    #     employee_page.get_fullName().send_keys('Akash G Krishnan ak')
    #     employee_page.get_email().click()
    #     employee_page.get_email().send_keys('akash.krishnan1112@mailinator.com')
    #     employee_page.get_password().send_keys('Testing@123')
    #     employee_page.get_confirm_password().send_keys('Testing@123')
    #     employee_page.get_signup_button().click()
    #     sleep(3)
    #     assert 'Click on the verification link to activate your account.' in employee_page.get_success_modal().text
    #     employee_page.get_success_confirm().click()
    #     sleep(2)



    def test_employer_signIn(self):
        home_page = FmHomePage(self.driver)
        home_page.get_employer_sign_in().click()
        sleep(5)
        child_window = self.driver.window_handles[-1]
        self.driver.close()
        self.driver.switch_to.window(child_window)
        sign_in = SignInPage(self.driver)
        sign_in.get_email_field().click()
        sign_in.get_email_field().send_keys('akash.krishnan@innovationm.com')
        sign_in.get_password_field().send_keys('Test@123')
        sign_in.get_login_button().click()
        sleep(7)
        employer_home = EmployerHome(self.driver)
        assert employer_home.get_new_interview().text == 'New Interview'
        assert employer_home.get_add_deposit().text == 'Add Deposit'
        assert 'Security Deposit Balance:' in employer_home.get_security_deposit().text

    def test_create_job_profile(self):
        pass


    def test_create_candidate(self):
        home_page = FmHomePage(self.driver)
        home_page.get_employer_sign_in().click()
        sleep(5)
        child_window = self.driver.window_handles[-1]
        self.driver.close()
        self.driver.switch_to.window(child_window)
        sign_in = SignInPage(self.driver)
        sign_in.get_email_field().click()
        sign_in.get_email_field().send_keys('akash.krishnan@innovationm.com')
        sign_in.get_password_field().send_keys('Test@123')
        sign_in.get_login_button().click()
        sleep(7)






    def test_schedule_interview(self):
        home_page = FmHomePage(self.driver)
        home_page.get_employer_sign_in().click()
        sleep(5)
        child_window = self.driver.window_handles[-1]
        self.driver.close()
        self.driver.switch_to.window(child_window)
        sign_in = SignInPage(self.driver)
        sign_in.get_email_field().click()
        sign_in.get_email_field().send_keys('akash.krishnan@innovationm.com')
        sign_in.get_password_field().send_keys('Test@123')
        sign_in.get_login_button().click()
        sleep(7)
        employer_home = EmployerHome(self.driver)
        employer_home.get_new_interview().click()





