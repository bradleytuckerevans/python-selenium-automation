# Created by bradevans at 2/23/2022
Feature: Tests for Amazon search
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon
    When Search for coffee
    Then Verify search results are shown for "coffee"


  Scenario: User can see language options
    Given Open Amazon
    When Hover over Language options
    Then Verify Spanish option present

  Scenario Outline: User can select and search in a department
    Given Open Amazon
    When Select department by alias <alias>
    And Search for Faust
    Then Verify <department> department is selected


    Examples:
      | alias         | department |
    | audible        | audible |
    | stripbooks  | books |


  Scenario: User select and search in Pet Supplies
    Given Open Amazon
    When Select Pet Supplies department
    And Search for Kong
    Then Verify Pet Supplies department is correct

  Scenario: User can see New Arrivals
    Given  Open Amazon Hoodie product page
    When Hover over New Arrivals
    Then Verify Deals are Present

