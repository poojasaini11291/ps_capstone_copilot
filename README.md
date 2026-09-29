# ps_capstone_copilot

This repository demonstrates an agentic SDLC workflow for a small online calculator web application. The project uses a simple calculator as the use case for requirements capture, architecture definition, design review, implementation planning, verification, and pull request documentation.

## Project goal

The application provides a simple browser-based calculator that supports basic arithmetic operations such as addition, subtraction, multiplication, division, clear, and decimal input. The goal is to model how a small product idea can move through a structured, human-guided software delivery lifecycle using GitHub Copilot.

## Project structure

```text
.
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/
│       └── ci.yml
├── calculator_app/
│   ├── app.js
│   ├── index.html
│   └── styles.css
├── docs/
│   ├── requirements.md
│   ├── architecture.md
│   ├── design-review.md
│   ├── impl-plan.md
│   ├── pr-description.md
│   └── sdlc/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── main.py
│   ├── sync_service.py
│   └── validator.py
├── tests/
│   ├── test_calculator.py
│   ├── test_integration.py
│   ├── test_sync_service.py
│   └── test_validator.py
├── sample_data/
│   ├── source/
│   └── output/
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Example product scope

The calculator web app should include:

- numeric buttons for 0-9
- decimal input support
- arithmetic operations: +, -, *, /
- clear/reset functionality
- evaluation of the entered expression
- graceful handling of invalid expressions and division by zero
- a responsive layout suitable for browser use

## Running the calculator app

Open the app directly in a browser:

```bash
python -m http.server 8000
```

Then visit:

```text
http://localhost:8000/calculator_app/
```

## Running tests

```bash
pytest -q
```

## SDLC flow followed in this project

1. Requirements capture
2. Architecture definition
3. Design review
4. Implementation planning
5. Implementation
6. Review and verification
7. Pull request preparation

## Final deliverables

The repository includes the required SDLC artifacts in the docs folder and a pull request summary in:

- [docs/pr-description.md](docs/pr-description.md)
- [.github/pull_request_template.md](.github/pull_request_template.md)

## Notes

This repository is intentionally compact and production-minded, making it suitable for a GitHub Copilot capstone demonstration using a simple calculator web application as the example use case.
