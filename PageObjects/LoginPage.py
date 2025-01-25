from PageObjects.DashboardPage import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, userName, userPassword):
        self.page.get_by_placeholder("Username").fill(userName)
        self.page.get_by_placeholder("Password").fill(userPassword)
        self.page.get_by_role("button").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage
