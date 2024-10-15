Feature: User Registration

  Scenario: Register a new user with valid details
    Given I have the following user details
      | username     | password    | email               |
      | johndoe      | Passw0rd!   | johndoe@example.com |
      | janedoe      | SecurePass1 | janedoe@example.com |
    When I register the user
    Then the registration should be successful

  Scenario: Attempt to register a user with missing details
    Given I have the following user details
      | username | password    | email               |
      | johndoe  | Passw0rd!   |                     |
      |          | SecurePass1 | janedoe@example.com |
    When I register the user
    Then the registration should fail with an error message
