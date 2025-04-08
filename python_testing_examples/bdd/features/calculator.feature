Feature: Basic calculator

  Scenario: Add two numbers
    Given the calculator is running
    When I add 2 and 3
    Then the result should be 5
