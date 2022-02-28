VANITY QUEST README

LAST PYTHON VERSION USED
3.9.6

DEPENDENCIES
Pyinstaller version 4.3 is to be used for compiling to executables.

STANDARD LIBRARY MODULES USED
- pickle (for saving game progress)
- sys (for the exit function that works with compiled executables as
the builtin exit/quit functions are designed for interpreter sessions)
- textwrap (for dedenting long strings)
- unittest

ABOUT
Vanity Quest is built up to the third chapter of the storyline and tested up to the first. 
The executable version in the folder named dist is compiled for Windows, though
I've only tested it on one machine.

The project is fit to run from source code using the Python interpreter. The steps
are:

1) Clone this repo.
2) Run main.py using the Python interpreter.
3) If there are errors, check that it doesn't have to do with a mismatch for the last
Python version used to develop this project (see "LAST PYTHON VERSION USED"). I'd be
interested to see reports of any other errors.

Game saves are created using the pickle module from the Python standard library.

TESTING

To run the unit tests, be sure to navigate to the root directory. From there, use
the command `python -m unittest tests/test_everything.py` (for Windows) or
`python3 -m unittest tests/test_everything.py` (for Mac/Linux). To run an individual
unit test, replace the "test_everything.py" with the chosen test script in the
above command.

Here's a unit testing checklist to use:
1) Objects are initialized with the expected values and attributes.
2) Functions that only output text are called when the associated input is made
(by making them MagicMock objects using the @patch decorator and checking they
were called using their assert_called_once method).
3) If a function mutates a variable, the variable is tested for a new value
using assertEqual.
4) If a function's behaviour is conditional, make sure that it does what is expected
under every condition.
5) If a function results in another function call, that call should be made a mock,
and its function should be tested individually.
6) If additional test tools need to be created, such as by modifying unittest features,
include them in tests/vanity_test_tools.py.
