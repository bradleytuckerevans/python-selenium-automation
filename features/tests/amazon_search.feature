# Created by bradevans at 2/23/2022
Feature: Tests for Amazon search
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon
    When Search for coffee
    Then Verify search results are shown for "coffee"