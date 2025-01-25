from playwright.sync_api import expect, Page
from PageObjects.BuzzPage import BuzzPage
from PageObjects.PIMPage import PIMPage
from PageObjects.TimeSheetPage import TimeSheetPage


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

    def verifyUserLoggedIn(self):
        expect(self.page.locator(".oxd-brand-banner")).to_be_visible()

    def verifyInValidLoginErrorMessage(self):
        expect(self.page.get_by_text("Invalid credentials")).to_be_visible()

    def selectPIMNavOption(self):
        self.page.get_by_role("link", name="PIM").click()
        PIMpage = PIMPage(self.page)
        return PIMpage

    def selectBuzzNavOption(self):
        self.page.get_by_role("link", name="Buzz").click()
        buzzPage = BuzzPage(self.page)
        return buzzPage

    def selectTimeNavOption(self):
        self.page.get_by_role("link", name="Time").click()
        timeSheetPage = TimeSheetPage(self.page)
        return timeSheetPage
