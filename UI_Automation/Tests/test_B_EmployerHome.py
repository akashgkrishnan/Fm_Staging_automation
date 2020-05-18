from csv import reader
from csv import writer
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UI_Automation.pageObjects.EmployerCandidate import EmployerCandidate
from UI_Automation.pageObjects.EmployerHome import EmployerHome
from UI_Automation.pageObjects.EmployerScheduleInterview import ScheduleInterview
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
        with open('..\TestData\login.txt') as file:
            csv_Reader = list(reader(file))[::-1]
            self.email =csv_Reader[1][0]
            self.password = csv_Reader[1][1]
        home_page = FmHomePage(self.driver)
        home_page.get_employer_sign_in().click()
        sleep(3)
        child_window = self.driver.window_handles[-1]
        self.driver.close()
        self.driver.switch_to.window(child_window)
        sign_in = SignInPage(self.driver)
        sign_in.get_email_field().click()
        sign_in.get_email_field().send_keys(self.email)
        sign_in.get_password_field().send_keys(self.password)
        sign_in.get_login_button().click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Setup Your Account'))
        )

    def test_home_link_text(self):
        self.login()

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
        #job_profile.get_min_exp_field().send_keys('1 Year')
        enter_skills = job_profile.get_skills_field()
        enter_skills.send_keys('Java')
        enter_skills.send_keys(Keys.ENTER)
        enter_skills = job_profile.get_skills_field()
        enter_skills.send_keys('Core')
        enter_skills.send_keys(Keys.ENTER)
        job_profile.get_submit_job_profile().click()
        sleep(2)

    def test_create_candidate(self):
        self.login()
        employer_home = EmployerHome(self.driver)
        employer_home.get_candidate_profile().click()
        candidate_create = EmployerCandidate(self.driver)
        candidate_create.get_create_candidate().click()
        candidate_create.get_candidate_name_field().send_keys('Akash')
        candidate_create.get_candidate_mail().send_keys('akash@mailinator.com')
        candidate_create.get_candidate_phone_field().send_keys('8130233807')
        candidate_create.get_upload_resume().send_keys('D:/Akash/FoxMatrix_UIAutomation/UI_Automation/TestData/Akash-Resume.pdf')
        sleep(8)

    def test_admin_security_deposit(self):
        self.login()
        employer_home = EmployerHome(self.driver)
        employer_home.get_admin().click()
        employer_home.get_security_deposit().click()
        sleep(3)

    def test_admin_invoice(self):
        self.login()
        employer_home = EmployerHome(self.driver)
        employer_home.get_admin().click()
        employer_home.get_invoices().click()
        sleep(3)


    def test_reset_password(self):
        self.login()
        employer_home = EmployerHome(self.driver)
        employer_home.get_reset_password().click()
        sleep(3)
        employer_home.get_current_password().send_keys(self.password)
        self.new_password = '123@Testing'
        employer_home.get_new_password().send_keys(self.new_password)
        employer_home.get_confirm_password().send_keys(self.new_password)
        employer_home.get_password_reset_save_btn().click()
        with open('..\TestData\login.txt', 'a') as file:
            csv_writer = writer(file)
            csv_writer.writerow([self.email, self.new_password])

        sleep(10)

    def test_helpFeedback(self):
        self.login()
        employer_home = EmployerHome(self.driver)
        employer_home.get_help_and_feedback().click()
        employer_home.get_feedback_box().send_keys()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder = 'Write your query/feedback here...']"))
        )
        employer_home.get_feedback_box().send_keys("Akash g Krishnan Akash G Krishnan Akash G Krishana krishnanasskasdhkjahdkj")
        employer_home.get_feedback_submit().click()
        employer_home.get_success_ok_button().click()

    def test_schedule_interview(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))
        )
        self.email = 'akash.krishnan@innovationm.com'
        self.password = 'NewTesting@123'
        home_page = FmHomePage(self.driver)
        home_page.get_employer_sign_in().click()
        sleep(3)
        child_window = self.driver.window_handles[-1]
        self.driver.close()
        self.driver.switch_to.window(child_window)
        sign_in = SignInPage(self.driver)
        sign_in.get_email_field().click()
        sign_in.get_email_field().send_keys(self.email)
        sign_in.get_password_field().send_keys(self.password)
        sign_in.get_login_button().click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Setup Your Account'))
        )
        employer_home = EmployerHome(self.driver)
        employer_home.get_new_interview().click()
        sleep(3)
        schedule_interview = ScheduleInterview(self.driver)
        schedule_interview.get_select_first_job_profile().click()
        schedule_interview.get_next_button().click()
        schedule_interview.get_get_telephonic_radio_mode().click()
        schedule_interview.get_proceed_button().click()
        schedule_interview.get_select_first_candidate_profile().click()
        schedule_interview.get_next_button().click()
        schedule_interview.get_select_first_interviewer().click()
        schedule_interview.get_availability_button().click()
        schedule_interview.get_select_first_availability().click()
        schedule_interview.get_confirm_availability_button().click()
        schedule_interview.get_next_button().click()
        sleep(4)






