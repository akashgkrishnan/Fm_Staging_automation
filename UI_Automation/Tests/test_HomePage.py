from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UI_Automation.pageObjects.EmployerHome import EmployerHome
from UI_Automation.pageObjects.EmployerSignUp import EmployerSignUp
from UI_Automation.pageObjects.FmContactPage import FmContactPage
from UI_Automation.pageObjects.FmHomeEmployer import FmEmployerPage
from UI_Automation.pageObjects.FmHomePage import FmHomePage
from UI_Automation.pageObjects.EmployerSignInPage import SignInPage
from UI_Automation.utilities.BaseClass import BaseClass
from time import sleep

class TestFmHomePage(BaseClass):
    def random_mobile(self):
        return randint(1111111111, 5555555555)

    # def test_employer_FM_home(self):
    #     home_page = FmHomePage(self.driver)
    #     home_page.get_employer().click()
    #     employer_intro = FmEmployerPage(self.driver)
    #     employer_intro.get_request_demo().click()
    #     sleep(2)
    #     employer_intro.get_name_field().send_keys('Akash G Krishnan')
    #     employer_intro.get_email_field().send_keys('akash.k@oneassist.in')
    #     employer_intro.get_company_field().send_keys('KRISHNAN')
    #     employer_intro.get_company_website_field().send_keys('www.google.co.in')
    #     employer_intro.get_submit_demo().click()
    #     sleep(7)
    #
    # def test_contact_page(self):
    #     home_page = FmHomePage(self.driver)
    #     home_page.get_contact().click()
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//h1[contains(text(),"Hello!")]'))
    #     )
    #     contact_page = FmContactPage(self.driver)
    #     contact_page.get_name_field().send_keys("Akash G Krishnan")
    #     contact_page.get_company_field().send_keys("KRISHNAN")
    #     mobile = self.random_mobile()
    #     contact_page.get_email_field().send_keys(str(mobile) + '@mailinator.com')
    #     contact_page.get_phone_field().send_keys(mobile)
    #     contact_page.get_query_field().send_keys('test script run using selenium web driver api. test script run using selenium web driver api.')
    #     contact_page.get_submit_btn().click()
    #     sleep(5)
    #     assert contact_page.get_success_text().text == 'Thank You!'
    #
    # def test_interviewer_landing(self):
    #     home_page = FmHomePage(self.driver)
    #     home_page.get_interviewer().click()
    #     sleep(3)

    def test_employer_signUp(self):
        home_page = FmHomePage(self.driver)
        home_page.get_employer_signUp().click()
        sleep(5)
        child_window = self.driver.window_handles[-1]
        self.driver.close()
        self.driver.switch_to.window(child_window)
        employee_page = EmployerSignUp(self.driver)
        employee_page.get_company().send_keys('Automation Company 123')
        employee_page.get_fullName().send_keys('Akash G Krishnan ak')
        employee_page.get_email().click()
        mobile = self.random_mobile()
        email = str(mobile) + '@mailinator.com'
        employee_page.get_email().send_keys(email)
        password = 'Testing@123'
        employee_page.get_password().send_keys(password)
        employee_page.get_confirm_password().send_keys(password)
        employee_page.get_signup_button().click()
        sleep(3)
        assert 'Click on the verification link to activate your account.' in employee_page.get_success_modal().text
        employee_page.get_success_confirm().click()
        self.driver.get('https://www.mailinator.com/')
        self.driver.find_element_by_xpath("//input[@id='addOverlay']").send_keys(mobile)
        self.driver.find_element_by_xpath("//input[@id='addOverlay']").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('//tr[1]//td[3]').click()
        self.driver.find_element_by_xpath("//button[contains(text(),'Show Links')]").click()
        verification_url = self.driver.find_element_by_xpath("//div[@id='clicklinks']").text
        self.driver.get(verification_url)
        assert 'Welcome to FoxMatrix' in self.driver.find_element_by_xpath("//h2[contains(text(),'Welcome to FoxMatrix')]").text
        self.driver.find_element_by_xpath("//button[contains(text(),'Go to Login')]").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))
        )
        sign_in = SignInPage(self.driver)
        sign_in.get_email_field().click()
        sign_in.get_email_field().send_keys(email)
        sign_in.get_password_field().send_keys(password)
        sign_in.get_login_button().click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Setup Your Account')]"))
        )



    # def test_employer_signIn(self):
    #     home_page = FmHomePage(self.driver)
    #     home_page.get_employer_sign_in().click()
    #     sleep(5)
    #     child_window = self.driver.window_handles[-1]
    #     self.driver.close()
    #     self.driver.switch_to.window(child_window)
    #     sign_in = SignInPage(self.driver)
    #     sign_in.get_email_field().click()
    #     sign_in.get_email_field().send_keys('akash.krishnan@innovationm.com')
    #     sign_in.get_password_field().send_keys('Test@123')
    #     sign_in.get_login_button().click()
    #     sleep(7)
    #     employer_home = EmployerHome(self.driver)
    #     assert employer_home.get_new_interview().text == 'New Interview'
    #     assert employer_home.get_add_deposit().text == 'Add Deposit'
    #     assert 'Security Deposit Balance:' in employer_home.get_security_deposit().text







