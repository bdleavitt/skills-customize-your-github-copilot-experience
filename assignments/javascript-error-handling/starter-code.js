// Starter code for JavaScript Error Handling assignment

function validateAge(age) {
  // TODO: Check that age is a number, not empty, and not negative.
  // Throw a descriptive error if invalid.
  // Return a success message if valid.
  return "Age is valid.";
}

function getStudentGrade(student) {
  // TODO: Check that student is an object and contains a valid grade.
  // Throw an error if required data is missing or malformed.
  // Return the student's grade.
  return student.grade;
}

function calculate(a, b, operator) {
  // TODO: Handle invalid operator input and division by zero.
  // Use try/catch and throw errors for invalid conditions.
  return null;
}

// Example usage
try {
  console.log(validateAge(18));
  console.log(getStudentGrade({ name: "Sam", grade: "A" }));
  console.log(calculate(10, 2, "+"));
} catch (error) {
  console.error("Caught an error:", error.message);
}
