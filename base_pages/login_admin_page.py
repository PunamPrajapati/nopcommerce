from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginAdminPage:
    username_id = "Email"
    password_id = "Password"
    btn_login_xpath = "//button[normalize-space()='Log in']"
    btn_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout_btn(self):
        logout_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_logout_xpath)))
        logout_link.click()