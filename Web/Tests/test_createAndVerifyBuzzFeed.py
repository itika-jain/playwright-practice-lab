from PageObjects.LoginPage import LoginPage
from lorem import sentence


def test_createAndVerifyBuzzFeed(browserInstance):
    randomSentence = sentence()

    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login("Admin", "admin123")
    buzzPage = dashboardPage.selectBuzzNavOption()
    buzzPage.createPost(randomSentence)
    buzzPage.verifyPostCreated(randomSentence)
