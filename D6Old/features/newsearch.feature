Feature: search functionality

  Scenario: search for a product in ebay home page
    Given the user in the home page
    When the search text is entered
               | searchtext|
               |  samsung |
    And the search button is clicked
    Then the Search results page should be displayed



