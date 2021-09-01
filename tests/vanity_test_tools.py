from unittest.mock import MagicMock, Mock

def assert_no_call(self, *args, **kwargs):
    """
    Use this function to assert that a mock object was not called with
    the arguments specified.
    """
    # Adapted from: https://stackoverflow.com/questions/54838354/python-how-can-i-assert-a-mock-object-was-not-called-with-specific-arguments
    try:
        self.assert_any_call(*args, **kwargs)
    except AssertionError:
        return
    raise AssertionError(f"Expected {args, kwargs} not to have been passed to call.")

# As long as this module is imported, the function will be part
# of any mock object created during testing.
Mock.assert_no_call = assert_no_call
MagicMock.assert_no_call = assert_no_call

def test_ambient_inputs(dict_, scene, function, mock_print):
    """
    Some inputs in scenes have outcomes that simply
    print a message fetched from a dictionary.
    This function takes those elements as arguments
    and tests that the expected message was
    printed.
    """
    for word in dict_:
        scene.action = word
        function()
        mock_print.assert_called_with("\n" + dict_.get(word))