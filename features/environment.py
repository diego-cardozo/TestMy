from browser import Browser
from pages.home_page import HomePage


def before_all(context):
    """
    Create all used WebPage classes
    """
    context.browser = Browser()
    context.home_page = HomePage()


def after_all(context):
    """
    Log out user and close Web Browser
    """
    #context.admin_page.log_off()
    #context.browser.close()
