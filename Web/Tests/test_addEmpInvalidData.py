import names
from PageObjects.LoginPage import LoginPage


def test_addEmpInvalidData(browserInstance):
    name = names.get_first_name()

    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login("Admin", "admin123")
    PIMpage = dashboardPage.selectPIMNavOption()
    addEmployeePage = PIMpage.selectAddEmployeeButton()
    addEmployeePage.addInvalidEmpDetails(name)
