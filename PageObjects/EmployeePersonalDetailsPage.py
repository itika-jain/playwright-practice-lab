from playwright.sync_api import Page
from PageObjects.EmployeeListPage import EmployeeListPage


class EmployeePersonalDetailsPage:

    def __init__(self, page: Page):
        self.page = page

    def saveEmployeePersonalDetails(self):
        self.page.get_by_role("button", name=" Save ").nth(0).click()
        self.page.get_by_role("link", name="Employee List").click()
        employeeListPage = EmployeeListPage(self.page)
        return employeeListPage
