from playwright.sync_api import Page
from PageObjects.AddEmployeePage import AddEmployeePage


class PIMPage:

    def __init__(self, page: Page):
        self.page = page

    def selectAddEmployeeButton(self):
        self.page.get_by_role("button", name=" Add ").click()
        addEmployeePage = AddEmployeePage(self.page)
        return addEmployeePage
