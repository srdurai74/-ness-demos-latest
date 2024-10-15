Feature: login functionality

  @regressiontest
  Scenario: User logs in with valid credentials
    Given I am on the login page
    When I enter username in the username field
    And I enter password in the password field
    And I click the login button
    Then I should see the welcome page
