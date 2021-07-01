CONTENTS
1. TESTING

====

1. TESTING

When it comes to creating tests for Vanity Quest the developer needs to ask himself a few questions,
which have been sourced from: https://realpython.com/python-testing/


Question One: What Do I Want to Test?

Here is a list of everything that has been tested as of version 1.0:

scene_test.py
– init_tester: 
– Whether the Scene instance attributes are created with the expected values.
– Whether any inputs shared between scenes throws an error.
– Whether a save file is created without error.
– Whether a save file is loaded without error, and retains its states.

scene1_test.py
– Whether any parent inputs, or inputs unique to scene 1, throw an error.

Question Two: Is It a Unit Test or an Integration Test?

scene_test.py
It's both. Scene parent class is tested on its own. An instance of it is created for testing purposes
only. In fact, no such instance exists in the actual game's modules, because its purpose is only as a
parent class.
	Child scenes are then tested, both with the parent inputs, and every possible combination
of their unique inputs.

