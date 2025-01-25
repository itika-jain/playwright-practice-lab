from playwright.sync_api import Page


class BuzzPage:

    def __init__(self, page: Page):
        self.page = page

    def createPost(self, randomSentence):
        self.page.get_by_placeholder("What's on your mind?").fill(randomSentence)
        self.page.locator(".oxd-buzz-post-slot").click()

    def verifyPostCreated(self, randomSentence):
        postContent = self.page.locator(".orangehrm-buzz-post-body-text").nth(0).text_content()
        assert randomSentence == postContent
