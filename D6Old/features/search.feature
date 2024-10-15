
Feature: search functionality

  @smoketest
  Scenario Outline: search for a product in ebay home page
    Given I am on the home page
    When I fill in search field with Samsung
    And select a "<category>"
    And I click search button
    Then I should see Search results page for Samsung
    Examples:
      | category |
      | Books |
      | Cell Phones & Accessories |



