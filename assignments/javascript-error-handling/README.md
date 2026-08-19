# 📘 Assignment: JavaScript Error Handling

## 🎯 Objective

Learn how to write safer JavaScript by handling exceptions, validating input, and giving users clear feedback instead of crashing the program.

## 📝 Tasks

### 🛠️ Validate User Input

#### Description
Create a small JavaScript function that reads a user’s age and checks whether it is valid before continuing.

#### Requirements
Completed program should:

- Accept a value such as `age` and verify it is a number
- Reject `NaN`, empty values, and negative numbers with a clear error message
- Use `try` and `catch` to handle bad input without crashing the script
- Return a friendly message when the value is valid

### 🛠️ Handle File and Data Errors Safely

#### Description
Write a program that reads a JSON-like student record and handles missing or malformed data gracefully.

#### Requirements
Completed program should:

- Read a data object containing values such as `name`, `grade`, and `id`
- Throw an error when a required field is missing or not in the expected type
- Catch the error and print a helpful explanation for the user
- Avoid silent failures by logging or returning a meaningful message

### 🛠️ Practice Defensive Coding

#### Description
Improve a small calculator so it handles unexpected input in a controlled way.

#### Requirements
Completed program should:

- Support addition, subtraction, multiplication, and division
- Detect invalid operators and division by zero
- Use `throw new Error(...)` for invalid conditions
- Catch the exceptions and display a clear user-facing result
- Explain in comments why each check is important

### 🛠️ Reflection

#### Description
Review the differences between a crash, a handled error, and a validation message.

#### Requirements
Completed program should:

- Write a short paragraph explaining when to use `try/catch`
- Explain why validation is better than relying on a program to fail later
- Describe one example where proper error handling improves user experience

