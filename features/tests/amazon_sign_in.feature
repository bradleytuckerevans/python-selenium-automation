# Created by bradevans at 3/1/2022
Feature: Amazon Sign In tests
  # Enter feature description here

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon
    When Click on Button from SignIn popup
    Then Verify Sign In page is opened
