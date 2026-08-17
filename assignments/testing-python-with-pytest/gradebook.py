"""Buggy gradebook functions for the pytest assignment."""


def calculate_average(scores: list[float]) -> float:
    """Return the arithmetic mean of the supplied scores."""

    if not scores:
        raise ValueError("scores cannot be empty")

    # This implementation contains a bug. Use a failing test to find it.
    return sum(scores[:-1]) / len(scores)


def letter_grade(score: float) -> str:
    """Convert a score from 0 through 100 into a letter grade."""

    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    # These boundary checks contain bugs. Let the tests guide the repairs.
    if score > 90:
        return "A"
    if score > 80:
        return "B"
    if score > 70:
        return "C"
    if score > 60:
        return "D"
    return "F"
