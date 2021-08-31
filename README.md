VANITY QUEST README

PYTHON VERSION USED
3.9.6

DEPENDENCIES
Pyinstaller version 4.3 is to be used for compiling to executables.

STANDARD LIBRARY MODULES USED
- pickle (for saving game progress)
- sys (for the exit function that works with compiled executables as
the builtin exit/quit functions are designed for interpreter sessions)
- textwrap (for dedenting long strings)
- unittest

Instructions:
Vanity Quest is built up to the third chapter of the storyline and tested up to the first.
Contributions are welcomed, whether you want to add to the story or contribute
code (or both, as they go hand-in-hand for this project). The guidelines are
only to use common sense and follow PEP 8 as far as it makes sense to you to do
so. Also see the "TESTING" section.

An executable is expected to be compiled for Windows devices as I have yet to achieve
compiling for Mac on a Windows machine using Pyinstaller.

The project is fit to run from source code using the Python interpreter. The steps
are:

1) Get the appropriate version of Python at python.org.
2) Clone this repo.
3) From the terminal, navigate inside the project folder.
4) Run the main.py file. The command is `python main.py` for Windows and
`python3 main.py` for Mac/Linux.

Save games are created using the pickle module from the Python standard library.
Because the creative process is intertwined with determining the logic, and the
scope of the project is small, strings are stored in the scripts themselves, indented
and formatted for output using the textwrap module.

TESTING

To run the unit tests, be sure to navigate to the root directory. From there, use
the command `python -m unittest tests/test_everything.py` (for Windows) or
`python3 -m unittest tests/test_everything.py` (for Mac/Linux). To run an individual
unit test, replace the asterisk in that command with the chosen script.

The unit tests test (and should continue to test) that:
1) Objects are initialized with the expected values and attributes.
2) Functions that only output text are called when the associated input is made
(by making them MagicMock objects using the @patch decorator and checking they
were called using their assert_called_once method).
3) If a function mutates a variable, the variable is tested for a new value
using assertEqual.
4) If a function's behaviour is conditional, make sure that does what is expected
under every condition.
5) If a function results in another function call, that call should be made a mock,
and its function should be tested individually.
6) If additional test tools need to be created, such as by modifying unittest features,
include them in tests/vanity_test_tools.py.
