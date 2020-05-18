from selenium.webdriver.common.by import By


class EmployerHome:

    admin = (By.ID, "dropMenu")
    security_deposit = (By.XPATH, "//span[contains(text(),'Security Deposit')]")
    my_invoice = (By.XPATH, "//span[contains(text(),'My Invoices')]")
    new_interview = (By.LINK_TEXT, 'New Interview')
    add_deposit = (By.LINK_TEXT, 'Add Deposit')
    job_profile = (By.XPATH, "//span[contains(text(),'Job Profile')]")
    candidate_profile = (By.XPATH, "//span[contains(text(),'Candidate Profile')]")
    dashboard = (By.XPATH, "//span[contains(text(),'Dashboard')]")
    help_feedback = (By.LINK_TEXT, "Help/Feedback")
    help_feedback_box = (By.XPATH, "//textarea[@placeholder = 'Write your query/feedback here...']")
    feedback_submit = (By.XPATH, "//button[@type='submit']")
    success_help_feedback_ok = (By.XPATH, "//span[contains(text(),'OK')]")
    reset_pass = (By.XPATH, "//span[contains(text(),'Reset Password')]")
    current_password = (By.ID, "_currentpassword")
    new_password = (By.ID, "_password")
    confirm_password = (By.ID, "_confirmpassword")
    password_reset_save_button = (By.XPATH, "//button[contains(text(), 'Save Changes')]")
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

    def get_help_and_feedback(self):
        return self.driver.find_element(*EmployerHome.help_feedback)

    def get_feedback_box(self):
        return self.driver.find_element(*EmployerHome.help_feedback_box)

    def get_feedback_submit(self):
        return self.driver.find_element(*EmployerHome.feedback_submit)

    def get_success_ok_button(self):
        return self.driver.find_element(*EmployerHome.success_help_feedback_ok)

    def get_admin(self):
        return self.driver.find_element(*EmployerHome.admin)

    def get_security_deposit(self):
        return self.driver.find_element(*EmployerHome.security_deposit)

    def get_invoices(self):
        return self.driver.find_element(*EmployerHome.my_invoice)

    def get_reset_password(self):
        return self.driver.find_element(*EmployerHome.reset_pass)

    def get_current_password(self):
        return self.driver.find_element(*EmployerHome.current_password)

    def get_new_password(self):
        return self.driver.find_element(*EmployerHome.new_password)

    def get_confirm_password(self):
        return self.driver.find_element(*EmployerHome.confirm_password)

    def get_password_reset_save_btn(self):
        return self.driver.find_element(*EmployerHome.password_reset_save_button)



