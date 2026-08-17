# 📘 Assignment: Testing Python with pytest

## 🎯 Objective

Write focused unit tests with pytest, use test failures to locate bugs, and correct a small gradebook module without changing its intended behavior.

## 📝 Tasks

### 🛠️	Write Your First Tests

#### Description
Complete the first tests for `calculate_average()` and learn how pytest reports passing and failing examples.

#### Requirements
Completed program should:

- Add at least three test functions whose names begin with `test_`
- Verify that `calculate_average([80, 90, 100])` returns `90`
- Verify the result for a list containing one score
- Use `pytest.approx()` for comparisons involving decimal results
- Run the test suite and read the failure messages before changing `gradebook.py`


### 🛠️	Test Boundaries and Errors

#### Description
Test important boundary cases and confirm that invalid input produces the expected exceptions.

#### Requirements
Completed program should:

- Verify that `letter_grade()` returns `"A"`, `"B"`, `"C"`, `"D"`, and `"F"` at the correct score boundaries
- Use `@pytest.mark.parametrize` to test multiple score and expected-grade pairs
- Verify that `calculate_average([])` raises `ValueError`
- Verify that `letter_grade()` raises `ValueError` for scores below `0` or above `100`
- Check at least one exception message with `pytest.raises(..., match=...)`


### 🛠️	Find and Fix the Bugs

#### Description
Use the failing tests as evidence to identify defects in `gradebook.py`, then make the smallest corrections needed.

#### Requirements
Completed program should:

- Correct the average calculation so it uses every score
- Correct all letter-grade boundary conditions
- Keep the provided function names and parameters unchanged
- Avoid hard-coding answers for individual test examples
- Pass every test in `test_gradebook.py`


### 🛠️	Add a Regression Test

#### Description
Add one final test that would fail if a corrected bug were accidentally introduced again.

#### Requirements
Completed program should:

- Add a clearly named regression test for one repaired defect
- Include a short comment identifying the bug the test prevents
- Keep each test focused on one behavior
- Finish with a test run in which all tests pass