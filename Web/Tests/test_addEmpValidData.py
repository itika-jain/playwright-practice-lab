import names
from PageObjects.LoginPage import LoginPage


def test_addEmpValidData(browserInstance):

    firstName = names.get_first_name()
    lastName = names.get_last_name()

    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login("Admin", "admin123")
    PIMpage = dashboardPage.selectPIMNavOption()
    addEmployeePage = PIMpage.selectAddEmployeeButton()
    employeePersonalDetailsPage = addEmployeePage.addNewEmployeeDetails(firstName, lastName)
    employeeListPage = employeePersonalDetailsPage.saveEmployeePersonalDetails()
    employeeListPage.searchEmployee(firstName, lastName)
