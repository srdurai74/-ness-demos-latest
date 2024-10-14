Feature: search functionality

  @smoke
  @regression
  Scenario Outline: Search for a product in ebay home page
    Given the user is on the ebay home page
    When the user searches for "samsung"
    And select a "<category>"
    And click the search button
    Then the search results page for samsung is displayed
    Examples:
      | category |
      | Books |
      | Cell Phones & Accessories |
