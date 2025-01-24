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
  - Both positive and negative test cases where applicable

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

Due Jan 31 by 19.00

1. What is it
2. What does it do
3. How does it work
4. Grant the right to use it
5. Don't change it

Testing with unittest Module in Python

## Tasks for this assignment

- Create a good README
- Write a statement of contributions for each team member
- Program should be functionally correct
- Program should be appropriately tested, with at least one unit test per LIC, and at least 2 tests (positive and negative) if applicable. WHAT SHOULD WE USE FOR TESTING? jUnit?
- Collaboration is well structured and traceable
- every commit is an atomic bug fix or feature with a clear commit message, including an appropriate commit prefix (feat, fix, doc, refactor)
- every commit reflects the commit message, and the fix or feature always has or modifies a test
- Commits are balanced among group members
- Assess and document in one paragraph our way of working

For P+

- most recent 25 commits are linked to an issue
- we have done something remarkable and mention it in our statement of contributions

## Things to do

- Decide the language, unit testing framework, and talk about strengths/weaknesses.
- Create issues for implementing the README, DECIDE functions/features and assign them to team members on Github
- Remember to: add functionality AND tests, make clear commit messages, communicate with group members for help
- Set up a timeline for finishing issues, integrating features, and completing the assignment

## Statement of Contributions

List each person and a description of their contributions.

## Statement of way of working

one paragraph based on https://www.omg.org/spec/Essence/1.2/PDF p.50 checklist
What state are you in? Why? What are obstacles to reach the next state?
