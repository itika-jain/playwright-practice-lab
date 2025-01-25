import json

import pytest
from PageObjects.LoginPage import LoginPage

with open("D:/Study/OrangeHRM/data/credentials.json") as f:
    login_data = json.load(f)
    user_credentials_list = login_data["user_credentials"]


@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_validLogin(browserInstance, user_credentials):
    userName = user_credentials["userName"]
    userPassword = user_credentials["userPassword"]

    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, userPassword)
    dashboardPage.verifyUserLoggedIn()
