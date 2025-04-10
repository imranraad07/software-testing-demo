Feature: Basic calculator

Scenario: Add two numbers
    Given I have numbers 2 and 3
    When I add them
    Then the result should be 5


Scenario: Add 3, 4 and 5
    Given I have number 3
    And I have number 4
    And I have number 5
    When I add all the numbers
    Then the result should be 12
