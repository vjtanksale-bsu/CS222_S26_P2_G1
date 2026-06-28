# CS222_S26_P2_G1

Story 2 implements a user input validation system for selecting the number of courses a student wants to take.

The system prompts the user to enter an integer value representing their desired course load. It validates that the input is an integer between 1 and 7. If the input is invalid (non-integer values, numbers less than 1, or greater than 7), the system displays an error message and continuously re-prompts the user until a valid input is provided.

The implementation follows TDD and Clean Code principles by separating responsibilities into three functions: input validation, data parsing, and user interaction loop. This ensures modularity, readability, and testability of the code.
