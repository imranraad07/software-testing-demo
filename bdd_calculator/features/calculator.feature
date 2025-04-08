Feature: Calculator operations

  Scenario: Add two numbers
    Given the calculator is running
    When I add 2 and 3
    Then the result should be 5

  Scenario: Multiply numbers with precedence
    Given the calculator is running
    When I evaluate "2 + 3 * 4"
    Then the result should be 14

  Scenario: Handle scientific notation
    Given the calculator is running
    When I evaluate "1e2 + 2e1"
    Then the result should be 120.0

  Scenario: Division with decimal precision
    Given the calculator is running with precision 3
    When I evaluate "10 / 3"
    Then the result should be 3.333
