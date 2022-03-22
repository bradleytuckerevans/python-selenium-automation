# Created by bradevans at 3/21/2022
Feature: Sign in page when clicking orders
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon
    When Click Amazon Orders link
    Then Verify Sign In page is opened