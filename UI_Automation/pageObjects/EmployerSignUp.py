from selenium.webdriver.common.by import By


class EmployerSignUp:
    company_name = (By.XPATH, '//label[@class="has-float-label"]')

    full_name = (By.XPATH, '//*[@id="employerForm"]/div[2]/div/div/label[1]/input')

    email = (By.NAME, 'email')

    password = (By.XPATH, '//*[@id="_password"]')

    confirm_password = (By.XPATH, '//*[@id="_confirmpassword"]')

    sign_up_btn = (By.XPATH, '//*[@id="employerForm"]/div[4]/button')

    login_url = (By.XPATH, '//*[@id="employerForm"]/div[4]/div/a')

    def __init__(self, driver):
        self.driver = driver

    def get_company(self):
        return self.driver.find_element(*EmployerSignUp.company_name)

    def get_fullName(self):
        return self.driver.find_element(*EmployerSignUp.full_name)

    def get_email(self):
        return self.driver.find_element(*EmployerSignUp.email)

    def get_password(self):
        return self.driver.find_element(*EmployerSignUp.password)

    def get_confirm_password(self):
        return self.driver.find_element(*EmployerSignUp.confirm_password)

    def get_signup_button(self):
        return self.driver.find_element(*EmployerSignUp.sign_up_btn)

    def get_login_url(self):
        return self.driver.find_element(*EmployerSignUp.login_url)

