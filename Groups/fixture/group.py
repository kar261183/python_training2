from selenium.webdriver.common.by import By

from Groups.model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php")
                and len(driver.find_elements(By.NAME, "new"))) > 0:
            driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        driver.find_element(By.NAME, "delete").click()
        self.return_to_group_page()

    def modify_group(self, new_group_data):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        driver.find_element(By.NAME, "update").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//*[@id='content']/form/span[1]/input").click()

    def return_to_group_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements(By.XPATH, "//*[@id='content']/form/span[1]/input"))

    def get_group_list(self):
        driver = self.app.driver
        self.open_group_page()
        groups = []
        for element in driver.find_elements(By.XPATH, '//*[@id="content"]/form/span'):
            text = element.text
            id = element.find_element(By.XPATH, "//*[@id='content']/form/span[1]/input").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups
