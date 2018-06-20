from behave import given, when, then
"""
Tests steps implementation
"""


@given('I open "{url}"')
def open_url(context, url):
    print("url " + url)
    context.browser.go_to(url)


@when('I create search "{text}"')
def step(context, text):
    context.home_page.set_text_to_search(text)


@then('I click in Iam Feeling Lucky button')
def step(context):
    context.home_page.click_iam_feeling_lucky_button()

