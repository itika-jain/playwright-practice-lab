import json
import pytest
from PageObjects.LoginPage import LoginPage

with open("D:/Study/OrangeHRM/data/credentials.json") as f:
    login_data = json.load(f)
    login_credentials_list = login_data['invalid_user_credentials']


@pytest.mark.parametrize('invalid_user_credentials', login_credentials_list)
def test_invalidLogin(browserInstance, invalid_user_credentials):
    userName = invalid_user_credentials["userName"]
    userPassword = invalid_user_credentials["userPassword"]

    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, userPassword)
    dashboardPage.verifyInValidLoginErrorMessage()
