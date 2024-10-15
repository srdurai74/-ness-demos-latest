Feature: User registration

  Scenario: Register a new user
    Given I have user data
      |username|password|email|
      |user1   |pass1   |user1@gmail.com|
      |user2   |pass2   |user1@gmail.com|
    When i register the user
    Then the user should be registered

    