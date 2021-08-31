from Universe.Scene import Scene
from Characters.PlayerCharacter import PlayerCharacter
from Characters.Metacy import Metacy
# vanity_test_tools module contains unittest.mock tools modified with new method
from tests.vanity_test_tools import Mock, MagicMock
from unittest.mock import patch
import textwrap
import unittest

class TestScene(unittest.TestCase):

    def setUp(self):
        # Initialize some things that are initialized in the main script
        # when the program runs normally.
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

        try:
            self.scene.enter()
        except SystemExit:
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
        self.scene.environment.append("Environmental changes.")
        self.scene.player.inventory.append("Picked-up items.")
        self.scene.player.mind.append("Knowledge the player gathered.")
        self.scene.player.power.append("Power the player acquired.")
        self.scene.plot_points.append("Events that occurred.")

        # Make sure the test save file does not overwrite the usual save file by
        # giving it a different name.
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

# Run unittest.main only if run independently. Otherwise, the
# test_everything script takes care of it.
if __name__ == "__main__":
    unittest.main()
