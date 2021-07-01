from unittest.mock import MagicMock, Mock

# Adapted from: https://stackoverflow.com/questions/54838354/python-how-can-i-assert-a-mock-object-was-not-called-with-specific-arguments
def assert_no_call(self, *args, **kwargs):
    try:
        self.assert_any_call(*args, **kwargs)
    except AssertionError:
        return
    raise AssertionError(f"Expected {args, kwargs} not to have been passed to call.")

Mock.assert_no_call = assert_no_call
MagicMock.assert_no_call = assert_no_call
