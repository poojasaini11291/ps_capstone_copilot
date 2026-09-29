from __future__ import annotations

import re

_TOKEN_PATTERN = re.compile(r"\d+(?:\.\d+)?|\.\d+|[()+\-*/]")
_OPERATOR_PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "u+": 3, "u-": 3}
_BINARY_OPERATORS = {"+", "-", "*", "/"}


def _tokenize(expression: str) -> list[str]:
    """Split an arithmetic expression into tokens."""
    cleaned = expression.strip()
    if not cleaned:
        raise ValueError("Expression is empty.")

    tokens: list[str] = []
    index = 0
    while index < len(cleaned):
        if cleaned[index].isspace():
            index += 1
            continue

        match = _TOKEN_PATTERN.match(cleaned, index)
        if match is None:
            raise ValueError("Expression contains invalid characters.")

        token = match.group(0)
        tokens.append(token)
        index = match.end()

    if not tokens:
        raise ValueError("Expression is empty.")

    return tokens


def _to_rpn(tokens: list[str]) -> list[str]:
    """Convert a token stream into reverse Polish notation."""
    output: list[str] = []
    operators: list[str] = []
    previous_token: str | None = None

    for token in tokens:
        if token not in _BINARY_OPERATORS and token not in {"(", ")"}:
            output.append(token)
            previous_token = token
            continue

        if token == "(":
            operators.append(token)
            previous_token = token
            continue

        if token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            if not operators:
                raise ValueError("Expression contains mismatched parentheses.")
            operators.pop()
            previous_token = token
            continue

        if token in {"+", "-"} and (previous_token is None or previous_token in {"(", "+", "-", "*", "/"}):
            token = "u-" if token == "-" else "u+"
        
        while operators and operators[-1] != "(" and _OPERATOR_PRECEDENCE[operators[-1]] >= _OPERATOR_PRECEDENCE[token]:
            output.append(operators.pop())

        operators.append(token)
        previous_token = token

    while operators:
        operator = operators.pop()
        if operator == "(":
            raise ValueError("Expression contains mismatched parentheses.")
        output.append(operator)

    return output


def _evaluate_rpn(tokens: list[str]) -> float:
    """Evaluate an expression in reverse Polish notation."""
    stack: list[float] = []

    for token in tokens:
        if token in {"u+", "u-"}:
            if not stack:
                raise ValueError("Expression is invalid.")
            value = stack.pop()
            stack.append(value if token == "u+" else -value)
            continue

        if token in _BINARY_OPERATORS:
            if len(stack) < 2:
                raise ValueError("Expression is invalid.")
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                stack.append(left / right)
            continue

        try:
            stack.append(float(token))
        except ValueError as exc:
            raise ValueError("Expression is invalid.") from exc

    if len(stack) != 1:
        raise ValueError("Expression is invalid.")

    return float(stack[0])


def evaluate_expression(expression: str) -> float:
    """Evaluate a basic arithmetic expression.

    Supported operations: +, -, *, /, parentheses, and decimal numbers.
    """
    tokens = _tokenize(expression)
    if not tokens:
        raise ValueError("Expression is empty.")

    rpn = _to_rpn(tokens)
    if not rpn:
        raise ValueError("Expression is empty.")

    result = _evaluate_rpn(rpn)
    return result
