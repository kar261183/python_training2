from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def logout(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_group_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def create_new_group(self, group):
        driver = self.driver
        self.open_group_page()
        driver.find_element(By.NAME, "new").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def open_group_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.ID, "LoginForm").click()
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook")

    def destroy(self):
        self.driver.quit()
