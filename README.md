# DD2480-DECIDE

A program implementing the DECIDE launch interceptor system that determines whether to launch an interceptor based on input radar tracking information.

## Requirements

- Python 3.11 or higher
- pip (Python package installer)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/DD2480-DECIDE.git
cd DD2480-DECIDE
```

2. Create and activate a virtual environment:

```bash
# On Unix/macOS:
python -m venv .venv
source .venv/bin/activate

# On Windows:
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Tests are written using Python's unittest framework. To run all tests:

```bash
python -m unittest discover test
```

## Project Structure

- `decide.py`: Main program logic
- `lib/`: Helper functions and utilities
- `test/`: Test files
  - One unit test per LIC (Launch Interceptor Condition)

## Development Guidelines

- Every commit should:
  - Be atomic (one feature or bug fix)
  - Have a clear commit message with appropriate prefix (feat, fix, doc, refactor)
  - Include or modify relevant tests
  - Be linked to an issue (for tracking)

## Statement of Contributions

[Team Member 1]:

- Implementation of ...
- Testing of ...

[Team Member 2]:

- Implementation of ...
- Testing of ...

[Continue for each team member]

## Way of Working

Our team is currently in the [state name] state according to the Essence standard. We have established clear communication channels, defined our development workflow, and set up the necessary tools and frameworks. Our main obstacles to reaching the next state include [obstacles]. We are actively working on addressing these challenges through [solutions/approaches].

## License

This project is part of the DD2480 course at KTH. All rights reserved.
