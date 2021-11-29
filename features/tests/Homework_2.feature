# Created by miche at 11/28/2021
Feature: # Test scenarios for search functionality

  Scenario: # User can search for solutions of cancelling an order on Amazon
    Given open Amazon help page
    When Input cancel order into search help library field
    And Click on search icon
    Then cancel items or orders text is present

