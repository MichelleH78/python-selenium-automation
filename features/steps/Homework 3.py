"""
Homework 3.1

Amazon logo -       By.class "a-icon a-icon-logo"
Create Account -    By.class "a-spacing-small"
Name -              By.id "ap_customer_name"
Email -             By.id "ap_email"
Password -          By.id "ap_password"
Re-Enter Pass -     By.id "ap_password_check"
Conditions of use - By.XPATH, ("//a[contains(@href, 'condition_of_use')]")
Privacy Notice -    By.XPATH  ("//a[contains(@href, 'notification_privacy_notice')]")
Sign in -           By.XPATH ("//a[contains(@href, '/ap/signin')]")

Homework 3.2


from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys


@given('Open Amazon help page')
def open_google(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')



@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(By.ID, "helpsearch")
    search.clear()
    search.send_keys(search_word)
    search.send_keys(Keys.ENTER)
    sleep(2)



@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"


@given('Open Amazon home page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')

@when('Click cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then("Page shows {expected_result}")
def verify_search_result(context, expected_result):
        actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
        expected_result = 'Your Amazon Cart is empty'
        assert expected_result == actual_result, f'error, actual {actual_result} did not match {expected_result}'

        """