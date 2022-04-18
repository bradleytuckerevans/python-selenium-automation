# Created by bradevans at 4/6/2022
Feature: Tests for DTN main page
  # Enter feature description here

  Scenario: User can see hamburger menu
    Given Open DTN
    Then Verify hamburger menu is present

  Scenario: User can see footer links for Industries and About
    Given Open DTN
    Then Verify 13 links are present


  Scenario: User can open Twitter footer link
    Given Open DTN
    And Store original window
    When Click on Twitter footer link
    And Switch to the new window
    Then Verify Twitter is open
    And Close Twitter
    And Return to original window


  Scenario: User can open Shipping from Hamburger Menu
    Given Open DTN
    When Click on hamburger link
    And Click on Shipping hamburger link
    Then Verify Shipping page is open

