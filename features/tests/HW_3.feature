# Created by miche at 12/26/2021
Feature: Homework 3 test cases


Scenario: User can find 'cancel order' link with search
    Given Open Amazon help page
    When Input cancel order into search field
    Then Product results for cancel+order are shown


Scenario: Verify Amazon cart is empty
    Given Open Amazon home page
    When Click cart icon
    Then Page shows {expected_result}

