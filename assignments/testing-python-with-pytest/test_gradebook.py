"""Complete these tests, then use the failures to repair gradebook.py."""

import pytest

from gradebook import calculate_average, letter_grade


def test_calculate_average_for_three_scores() -> None:
    # TODO: Replace the placeholder assertion with the expected average.
    assert calculate_average([80, 90, 100]) == 0


def test_calculate_average_for_decimal_result() -> None:
    # TODO: Use pytest.approx() to compare the expected decimal result.
    assert calculate_average([70, 75, 80]) == 0


def test_calculate_average_rejects_empty_list() -> None:
    # TODO: Use pytest.raises() and check the exception message.
    pytest.skip("Complete the empty-list exception test")


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        # TODO: Add boundary cases for A, B, C, D, and F grades.
        (100, "A"),
    ],
)
def test_letter_grade_boundaries(score: float, expected: str) -> None:
    assert letter_grade(score) == expected


@pytest.mark.parametrize("invalid_score", [-1, 101])
def test_letter_grade_rejects_invalid_scores(invalid_score: float) -> None:
    # TODO: Verify that invalid_score raises ValueError.
    pytest.skip("Complete the invalid-score exception test")


# TODO: Add one clearly named regression test after repairing gradebook.py.
