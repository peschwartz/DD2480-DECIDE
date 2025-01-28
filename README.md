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

## Statement of Contributions

[Carl ]:

- Implementation of ...
- Testing of ...

[Jacob ]:

- Implementation of ...
- Testing of ...

[Klara ]:

- Implementation of ...
- Testing of ...

[Phoebe ]:

- Implementation of LICs 3, 8, 13
- Testing of LIC3, 8, 13, PUM
- Implementation of PUM file with calculation function
- Implementation of PUM testing
- Implementation of the decide file and functions
- Implementation of the decide testing
-

As a group, we were very successful with our implementation of the DECIDE framework. Not only did we complete the functions and implement them correctly, we also learned and practiced good software engineering processes. We communicated frequently and met in person often. We set rules for how we wanted to create commits and issues and followed these practices throughout the implementation of our framework.

[Samuel ]:

- Implementation of LICs 0, 5, 10
- Testing of LICs 0, 5, 10
- Setting up initial testing skeletons for CMV and FUV as well as initial global variables
- Implementation of the FUV and LAUNCH computation functions
- Implementation of the FUV and LAUNCH tests
- Debugging and fixing the input parsing function + various bug fixes

## Way of Working

Our team is currently in the [state name] state according to the Essence standard. We have established clear communication channels, defined our development workflow, and set up the necessary tools and frameworks. Our main obstacles to reaching the next state include [obstacles]. We are actively working on addressing these challenges through [solutions/approaches].

## License

This project is part of the DD2480 course at KTH. All rights reserved.
