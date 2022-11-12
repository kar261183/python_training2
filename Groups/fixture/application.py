from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Groups.fixture.session import SessionHelper
from Groups.fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook")

    def destroy(self):
        self.driver.quit()
