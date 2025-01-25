from playwright.sync_api import Page, expect
from PageObjects.EmployeePersonalDetailsPage import EmployeePersonalDetailsPage


class AddEmployeePage:

    def __init__(self, page: Page):
        self.page = page

    def addNewEmployeeDetails(self, firstName, lastName):
        self.page.get_by_placeholder("First Name").fill(firstName)
        self.page.get_by_placeholder("Last Name").fill(lastName)
        self.page.get_by_role("button", name=" Save ").click()
        employeePersonalDetailsPage = EmployeePersonalDetailsPage(self.page)
        return employeePersonalDetailsPage

    def addInvalidEmpDetails(self, name):
        self.page.get_by_placeholder("First Name").fill(name)
        self.page.get_by_role("button", name=" Save ").click()
        expect(self.page.locator(".oxd-input-field-error-message")).to_be_visible()
