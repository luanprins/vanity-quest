from Universe.Scene import Scene
from Characters.PlayerCharacter import PlayerCharacter
from Characters.Metacy import Metacy
# vanity_test_tools module contains unittest.mock tools modified with new method
from tests.vanity_test_tools import Mock, MagicMock
from unittest.mock import patch
import textwrap
import unittest
# from unittest.mock import MagicMock, Mock, patch

# As Scene sets some of its values to player attributes,
# an instance of the player is created here.

# the TestCase base class represents the logical test units in the unittest universe.
# source: https://docs.python.org/3/library/unittest.html#unittest.TestCase

class TestScene(unittest.TestCase):

    # Note: adding __init__ caused problems: stackoverflow.com/questions/42790980/python-unittest-throws-uncaught-typeerror-init-takes-1-positional-argumen
    # (My error was almost identical to the one linked.)

    # "Test fixture" – prepare to perform tests (and cleanup after).
    # Would involve later-described setUp and tearDown methods.
    # source: https://docs.python.org/3/library/unittest.html

    def setUp(self):
        self.fairy = Metacy()
        self.player = PlayerCharacter()
        self.plot_points = []
        self.scene = Scene(self.player, self.plot_points, self.fairy)

    def test_init(self):
        """
        The values of instance attributes are either
        presets or passed-in values. This function checks
        that they have the expected values after initialization.
        """
        self.assertEqual(self.scene.environment, [])
        self.assertEqual(self.scene.player, self.player)
        self.assertEqual(self.scene.plot_points, self.plot_points)
        self.assertEqual(self.scene.fairy, self.fairy)

    @patch.object(PlayerCharacter, "show_inventory")
    @patch.object(Scene, "save_game")
    @patch.object(Scene, "load_game")
    @patch.object(Scene, "help_method")
    @patch("builtins.input", side_effect = ["help", "inventory",
                                            "save", "load", "exit"])
    def test_that_menu_functions_are_called(self, mock_input, mock_help_method,
                                            mock_load_game, mock_save_game,
                                            mock_show_inventory):
        """
        From the scene object's enter method, call every accepted
        input to check that the correlating method gets called.
        """
        # It's necessary to re-initialize the scene object for this
        # test because some of its methods, which have now been patched,
        # are stored in a dictionary during initialization and fetched
        # via the enter method.
        self.scene = Scene(self.player, self.plot_points, self.fairy)
        # These worked only the accepted_inputs attribute had to be moved
        # to be defined under the enter method because the objects stored
        # to the dictionary under __init__ kept the state that they were
        # in when the first instance of scene was created.
        # self.scene.help_method = MagicMock()
        # self.scene.load_game = MagicMock()
        # self.scene.player.show_inventory = MagicMock()
        # self.scene.save_game = MagicMock()
        # self.assertRaises(SystemExit, self.scene.enter)
        try:
            self.scene.enter()
        except SystemExit:
            # self.scene.help_method.assert_called_once()
            # self.scene.load_game.assert_called_once()
            # self.scene.player.show_inventory.assert_called_once()
            # self.scene.save_game.assert_called_once()
            mock_help_method.assert_called_once()
            mock_load_game.assert_called_once()
            mock_show_inventory.assert_called_once()
            mock_save_game.assert_called_once()

    def test_save_and_load(self):
        """
        The save file must be created when the save function is
        called. The object saved to it, when retrieved, must match
        the object initialized in setUp.
        """
        # self.scene.save_game.save_file = open("mock_savegame.pickle", "wb")
        # Note to self: this new_callable parameter will come in handy
        # if I want to start passing in my own custom mock objects from
        # a package specific to this project.
        # with patch("builtins.open", side_effect=open, *,
        #         file="mock_savegame.pickle", mode="wb"):
        self.scene.environment.append("Environmental changes.")
        self.scene.player.inventory.append("Picked-up items.")
        self.scene.player.mind.append("Knowledge the player gathered.")
        self.scene.player.power.append("Power the player acquired.")
        self.scene.plot_points.append("Events that occurred.")
        with patch("builtins.open", return_value=open("mock_savegame.pickle", "wb")):
            self.scene.save_game()
        with patch("builtins.open", return_value=open("mock_savegame.pickle", "rb")):
            loaded_object = self.scene.load_game()
            self.assertEqual(self.scene.environment, loaded_object.environment)
            self.assertEqual(self.scene.player.inventory, loaded_object.player.inventory)
            self.assertEqual(self.scene.player.mind, loaded_object.player.mind)
            self.assertEqual(self.scene.player.power, loaded_object.player.power)
            self.assertEqual(self.scene.plot_points, loaded_object.plot_points)

    @patch("builtins.print")
    @patch("builtins.input", side_effect = ["1", "2", "4", "3"])
    def test_help_method(self, mock_input, mock_print):
        """
        Test the help method responds as expected to inputs.
        Some prints must only be called under specific conditions.
        """
        self.scene.help_method()
        self.assertEqual(mock_print.call_count, 9)
        # Confirm fireball was not in player's power list and
        # the appropriate message was therefore printed.
        mock_print.assert_any_call(textwrap.dedent("""
                                        <Play more to unlock additional power 1>"""))
        mock_print.assert_no_call(textwrap.dedent("""
                                        fireball – turn foes or obstacles into piles of dust with
                                        this elemental ability which exhibits the fiery nature of
                                        your fairy companion's soul in an immolative orchestration."""))
        self.scene.player.power.append("fireball")
        with patch("builtins.input", side_effect = ["2", "3"]):
            self.scene.help_method()
            mock_print.assert_any_call(textwrap.dedent("""
                                        fireball – turn foes or obstacles into piles of dust with
                                        this elemental ability which exhibits the fiery nature of
                                        your fairy companion's soul in an immolative orchestration."""))



        # self.scene = Scene(self.player, self.plot_points, self.fairy)
        # We're only testing that these get called so they need nothing beyond
        # a mock return. Their proprietary class is re-initialized in setUp.

        # def stub():
        #     return "stub reached"

        # help_method = stub

        # self.scene.stub = lambda: "stub reached"

        # self.scene.help_method = self.scene.stub
        # self.scene.save_game = self.scene.stub
        # self.scene.load_game = self.scene.stub
        # self.scene.exit = self.scene.stub

        # Inputs that will result in a call of above menu_functions.
        # inputs = ["help"]
        # , "save", "load", "exit"

        # scene.enter calls the above functions with the above inputs,
        # so if its value is equal to their value, the calls were successful.
        # for word in inputs:
        #     with patch("builtins.input", side_effect = ["help", "exit"]):
        #         self.scene.enter()

    # # Reason builtins are under my module: stackoverflow.com/questions/44920344/is-it-possible-to-mock-the-builtin-len-function-in-python-3-6
    # # Must use full path when referring to modules with patch: stackoverflow.com/questions/61044136/modulenotfounderror-when-trying-to-use-mock-patch-on-a-method
    # @patch("Universe.Scene.Scene.help_method")
    # # So far no idea how to patch builtins but these might help.
    # # forbiddenfruit: https://github.com/clarete/forbiddenfruit

    # @patch("builtins.input")
    # @patch("builtins.exit")
    # def test_enter(self, mock_quit, mock_input, mocked_help_method):
    #     # consecutive call results – second call is from inside "method_a"
    #     mock_input.side_effect = ["help_method", "exit"]
    #     scene.enter()
    #     mocked_help_method.assert_called_once()

    # def test_enter(self):
    #     pass
    #     for i in ["help", "inventory", "save", "load", "exit"]:
    #     monkeypatch.setattr("builtins.input", input_iterator("help"))
    #     monkeypatch.setattr(scene_instance.help_method.help_act)
    #     try:
    #         scene_instance.enter()
    #     finally:
    #         pass

    # def test_help(monkeypatch):
    #     # for i in ["1", "2", "3"]:
    #     #     monkeypatch.setattr("builtins.input", input_iterator(i))
    #     #     scene_instance.help_method()

    # def test_save(self):
    #     # Should change the name of the savegame for the duration of the
    #     # test.

    # def test_load(self):

    #     # Should delete the saved game after we find out it works, so that
    #     # subsequent tests don't create more files.

# Note to self: this is so it runs as a test when you run the script from
# the command line.

if __name__ == "__main__":
    unittest.main()
