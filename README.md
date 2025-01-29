# DD2480-DECIDE
DECIDE is a program that implements a launch interceptor system, analyzing radar tracking data to determine whether an interceptor should be launched based on predefined safety and engagement conditions.

## Description
The function processes up to 100 radar-tracked objects and evaluates them against 15 Launch Interceptor Conditions (LICs). These conditions examine various factors, such as how close or far objects are, whether they form certain angles or shapes, and how they move relative to each other.

To make a final decision, DECIDE uses a Logical Connector Matrix (LCM) and a Preliminary Unlocking Vector (PUV). The LCM defines how conditions should be logically combined using AND/OR rules, while the PUV specifies which conditions must be considered. If all necessary conditions are satisfied, the function signals approval for missile launch; otherwise, the launch is blocked.

DECIDE acts as a crucial safeguard in the missile defense system, ensuring that interceptors are only deployed under appropriate circumstances.

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

## Running Tests

Tests are written using Python's unittest framework. To run all tests:

```bash
python -m unittest discover test
```

## Project Structure

- `lib/`: Helper functions and utilities
  - `util.py`: utility file for calculation functions
- `test/`: Test files
  - `main.py`: main testing file that calls each of our other testing files
  - `test_decide.in`: input file for the decide functionalities
  - `test_decide2.in`: input file for the decide functionalities
  - `test_decide3.in`: input file for the decide functionalities
  - `testcmv.py`: test functions for each of the 15 LICs
  - `testdecide.py`: test decide functions
  - `testfuv.py`: test function for the FUV vector
  - `testinputparse.py`: testing the decide_io.py functions
  - `testlaunch.py`: test functions for the LAUNCH decision
  - `testpum.py`: test functions for the PUM matrix
- `decide.py`: Main program logic
- `GLOBAL_VARS.py`: set up global variables available throughout all files
- `cmv.py`: file for calculating the CMV, includes functions for each of the 15 LICs
- `decide_io.py`: file to read and write input for the decide functionalities
- `framework.pdf`: pdf for the description of the decide functionalities
- `fuv.py`: file to calculate the FUV vector
- `launch.py`: file to calculate the launch string
- `pum.py`: file to calculate the PUM matrix

## Development Guidelines

- Every commit should:
  - Be atomic (one feature or bug fix)
  - Have a clear commit message with appropriate prefix (feat, fix, doc, refactor)
  - Include or modify relevant tests
  - Be linked to an issue (for tracking)
- Commenting Guidelines
  - Every file should have a comment describing what it does
  - Every function should have a comment describing what it does (even test functions)
  - Throughout functions, there should be comments to help follow the code
- Testing Guidelines
  - Functions should be tested accurately with both positive and negative assertions
  - New features should be tested extensively to ensure correctness

## License

This project is part of the DD2480 course at KTH. All rights reserved.
