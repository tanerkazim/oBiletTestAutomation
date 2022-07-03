from selenium.webdriver.common.by import By


class LoginPopup:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login-form')
    SIGNUP_BTN = (By.CSS_SELECTOR, 'a.sign-up')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register .container')
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '.register .email input')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, '.register .password input')
    REGISTER_BTN = (By.CSS_SELECTOR, '.register-button')

    def __init__(self, methods):
        self.methods = methods
        self.check()

    def check(self):
        self.methods.wait_for_element(self.LOGIN_FORM)
        self.methods.wait_for_element(self.SIGNUP_BTN)

    def navigate_to_signup(self):
        self.methods.wait_for_element(self.SIGNUP_BTN).click()

    def fill_email(self):
        self.methods.wait_for_element(self.REGISTER_EMAIL_INPUT).send_keys(self.methods.get_from_ini("register_email"))

    def fill_password(self):
        self.methods.wait_for_element(self.REGISTER_PASSWORD_INPUT).send_keys(self.methods.
                                                                              get_from_ini("register_password"))

    def complete_register(self):
        self.methods.wait_for_element(self.REGISTER_BTN).click()

    def login_form_presence(self):
        return self.methods.element_exists(self.LOGIN_FORM)

    def register_form_presence(self):
        return self.methods.element_exists(self.REGISTER_FORM)
