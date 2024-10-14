Feature: login functionality

  Background:
    Given the user is on the login page


  @smoke
  Scenario: User logs in with valid credentials
    When the username is entered
    And the password is entered
    And the login button is clicked
    Then the dashboard page is displayed

  @regression
  Scenario: User logs in with valid credentials
    When the user clicks the link in the footer
    Then a new window is displayed

