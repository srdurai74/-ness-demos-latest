Feature: search functionality

  Scenario: Search for a product in ebay home page
    Given the user is on the ebay home page
    When the search text and make year is entered
      | search text | make year  |
      | iphone | 2024            |
      | samsung | 2023           |

    And the search button is clicked
    Then the search results page is displayed

