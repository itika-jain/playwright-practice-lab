from playwright.sync_api import Page, expect


class TimeSheetPage:

    def __init__(self, page: Page):
        self.page = page

    def selectMyTimeSheetOption(self):
        self.page.locator(".oxd-topbar-body-nav-tab-item").get_by_text(" Timesheets ").click()
        self.page.locator(".oxd-topbar-body-nav-tab-link").get_by_text("My Timesheets").click()
        self.page.get_by_role("button", name=" Edit ").click()

    def editAndSubmitTimeSheet(self):
        self.page.get_by_placeholder("Type for hints...").fill("Internal")
        self.page.locator(".oxd-autocomplete-dropdown", has_text="Internal - Recruitment").click()
        self.page.locator(".oxd-select-text-input", has_text="-- Select --").click()
        self.page.locator(".oxd-select-dropdown", has_text="Job Analysis").click()
        for i in range(0, 7):
            self.page.locator("td.--duration-input").nth(i).type("8")
        self.page.get_by_role("button", name=" Save ").click()
        self.page.get_by_role("button", name=" Submit ").click()

    def checkStatusSubmitted(self):
        expect(self.page.locator(".orangehrm-timesheet-footer--title").get_by_text("Status: Submitted")).to_be_visible()
