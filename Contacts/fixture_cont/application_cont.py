from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Contacts.fixture_cont.session_cont import SessionHelper
from Contacts.fixture_cont.cont import ContHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.session_cont = SessionHelper(self)
        self.cont = ContHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook")

    def destroy(self):
        self.driver.quit()