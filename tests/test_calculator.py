import pytest

from src.calculator import evaluate_expression


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("2 + 3", 5.0),
        ("10 / 2", 5.0),
        ("2 * 3 + 4", 10.0),
        ("8 - 3 * 2", 2.0),
        ("( 10 + 2 ) / 3", 4.0),
    ],
)
def test_evaluate_expression_success(expression: str, expected: float):
    assert evaluate_expression(expression) == expected


def test_evaluate_expression_rejects_empty_input():
    with pytest.raises(ValueError, match="empty"):
        evaluate_expression("   ")


def test_evaluate_expression_rejects_invalid_expression():
    with pytest.raises(ValueError, match="invalid"):
        evaluate_expression("2 +")


def test_evaluate_expression_rejects_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate_expression("5 / 0")
