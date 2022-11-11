from selenium.webdriver.common.by import By


class ContHelper:
    def __init__(self, app):
        self.app = app

    def open_cont_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

    def create(self, cont):
        driver = self.app.driver
        self.open_cont_page()
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(cont.firstname)
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").clear()
        driver.find_element(By.NAME, "lastname").send_keys(cont.lastname)
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").clear()
        driver.find_element(By.NAME, "mobile").send_keys(cont.mobile)
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys(cont.email)
        driver.find_element(By.NAME, "submit").click()

