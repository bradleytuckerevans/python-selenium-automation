# Created by bradevans at 2/25/2022
Feature: Tests for Amazon Bestsellers
  # Enter feature description here

  Scenario: User can search for  Best seller links
    Given Open Amazon BestSellers
    Then Verify 5 links present