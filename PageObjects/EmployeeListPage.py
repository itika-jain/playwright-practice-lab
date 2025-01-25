from playwright.sync_api import Page, expect


class EmployeeListPage:

    def __init__(self, page: Page):
        self.page = page

    def searchEmployee(self, firstName, lastName):
        name = f"{firstName} {lastName}"

        self.page.get_by_placeholder("Type for hints...").nth(0).fill(name)
        self.page.get_by_role("button", name=" Search ").click()
        expect(self.page.get_by_text("No Records Found")).not_to_be_visible()
