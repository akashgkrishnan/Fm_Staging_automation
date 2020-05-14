from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UI_Automation.pageObjects.EmployerHome import EmployerHome
from UI_Automation.pageObjects.EmployerSignInPage import SignInPage
from UI_Automation.pageObjects.FmHomePage import FmHomePage
from UI_Automation.pageObjects.job_proflie import EmployerJobProfile
from UI_Automation.utilities.BaseClass import BaseClass
from time import sleep


class TestEmployerHome(BaseClass):
    def login(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))
        )
        home_page = FmHomePage(self.driver)
        home_page.get_employer_sign_in().click()
        sleep(3)
        child_window = self.driver.window_handles[-1]
        self.driver.close()
        self.driver.switch_to.window(child_window)
        sign_in = SignInPage(self.driver)
        sign_in.get_email_field().click()
        sign_in.get_email_field().send_keys('akash.krishnan@innovationm.com')
        sign_in.get_password_field().send_keys('Test@123')
        sign_in.get_login_button().click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'New Interview'))
        )


    # def test_home_link_text(self):
    #     self.login()

    def test_create_job_profile(self):
        self.login()
        employer_home = EmployerHome(self.driver)
        employer_home.get_job_profile().click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-warning']"))
        )
        job_profile = EmployerJobProfile(self.driver)
        job_profile.get_create_job_profile().click()

        job_profile.get_job_title_field().send_keys("JAVA DEVELOPER")
        job_profile.get_client_name_field().send_keys("Automation CLIENTS")
        job_profile.get_min_exp_down().click()

        enter_skills = job_profile.get_skills_field()
        enter_skills.send_keys('Java')
        enter_skills.send_keys(Keys.ENTER)
        enter_skills = job_profile.get_skills_field()
        enter_skills.send_keys('Core')
        enter_skills.send_keys(Keys.ENTER)
        job_profile.get_submit_job_profile().click()
        sleep(2)

    #
    # def test_create_candidate(self):
    #     self.login()
    #
    #
    # def test_schedule_interview(self):
    #     self.login()



