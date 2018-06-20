from browser import Browser


class HomePage(Browser):

    SEARCH_TEXT_BOX = '#lst-ib'
    IAM_FEELING_LUCKY = 'btnI'

    def set_text_to_search(self, text):
        """
        Open the Login page
        """
        search_text_box = self.query_selector_css(self.SEARCH_TEXT_BOX)
        search_text_box.send_keys(text)

    def click_iam_feeling_lucky_button(self):
        iam_feeling_lucky_button = self.query_selector_name(self.IAM_FEELING_LUCKY)
        iam_feeling_lucky_button.click()
