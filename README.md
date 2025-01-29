# DD2480-DECIDE
DECIDE is a program that implements a launch interceptor system, analyzing radar tracking data to determine whether an interceptor should be launched based on predefined safety and engagement conditions.

## Description
The function processes up to 100 radar-tracked objects and evaluates them against 15 Launch Interceptor Conditions (LICs). These conditions examine various factors, such as how close or far objects are, whether they form certain angles or shapes, and how they move relative to each other.

To make a final decision, DECIDE uses a Logical Connector Matrix (LCM) and a Preliminary Unlocking Vector (PUV). The LCM defines how conditions should be logically combined using AND/OR rules, while the PUV specifies which conditions must be considered. If all necessary conditions are satisfied, the Funal Unlocking Vector (FUV) signals approval for missile LAUNCH and returns YES; otherwise, the LAUNCH is blocked and returns NO.

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

MIT License

Copyright (c) 2025 Carl Lönnqvist, Jacob Molin, Klara Lindemalm, Phoebe Schwartz, Samuel Söderberg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
