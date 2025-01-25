from PageObjects.LoginPage import LoginPage


def test_createAndVerifyTimeSheet(browserInstance):
    loginPage = LoginPage(browserInstance)

    loginPage.navigate()
    dashboardPage = loginPage.login("Admin", "admin123")
    timeSheetPage = dashboardPage.selectTimeNavOption()
    timeSheetPage.selectMyTimeSheetOption()
    timeSheetPage.editAndSubmitTimeSheet()
    timeSheetPage.checkStatusSubmitted()
