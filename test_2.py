
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_create_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_group_page(driver)
        self.create_new_group(driver, name="12345", header="rrrrrr", footer="l;okljkhkh")
        self.return_to_group_page(driver)
        self.logout(driver)

    def test_create_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_group_page(driver)
        self.create_new_group(driver, name="", header="", footer="")
        self.return_to_group_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def create_new_group(self, driver, name, header, footer):
        driver.find_element(By.NAME, "new").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(footer)
        driver.find_element(By.NAME, "submit").click()


    def return_to_group_page(self, driver):
        driver.find_element(By.LINK_TEXT, "group page").click()

    def open_group_page(self, driver):
        driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, driver, username, password):
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.ID, "LoginForm").click()
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

