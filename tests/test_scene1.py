from Universe.Scene1_CaveMouth import Scene1_CaveMouth
from Universe.Scene2_CaveTunnel import Scene2_CaveTunnel
from Characters.PlayerCharacter import PlayerCharacter
from Characters.Metacy import Metacy
from tests.vanity_test_tools import Mock, MagicMock
from unittest.mock import patch
import textwrap
import unittest

class TestScene1(unittest.TestCase):

    def setUp(self):
        self.fairy = Metacy()
        self.player = PlayerCharacter()
        self.plot_points = []
        self.scene1 = Scene1_CaveMouth(self.player, self.plot_points, self.fairy)

    def test_init(self):
        """
        The values of instance attributes are either
        presets or passed-in values. This function checks
        that they have the expected values after initialization.
        """
        self.assertEqual(self.scene1.fairy, self.fairy)
        self.assertEqual(self.scene1.player, self.player)
        self.assertEqual(self.scene1.plot_points, self.plot_points)
        self.assertEqual(self.scene1.environment, [])
        self.assertEqual(self.scene1.name, "scene1")

    @patch.object(Scene1_CaveMouth, "fireball_outcomes")
    @patch.object(Scene1_CaveMouth, "straw_outcomes")
    @patch.object(Scene1_CaveMouth, "talk_outcomes")
    @patch.object(Scene1_CaveMouth, "interact_outcomes")
    @patch.object(Scene1_CaveMouth, "look_outcomes")
    @patch("builtins.print")
    @patch("builtins.input", side_effect = ["invalid input", "look", "interact",
                                            "talk", "straw", "fireball", "exit"])
    def test_enter(self, mock_input, mock_print, mock_look, mock_interact, mock_talk,
                    mock_straw, mock_fireball):
        """
        Scene 1's enter method extends the functionality of the
        parent class's method of the same name. This test checks
        that a series of inputs calls the correlating methods.
        """
        # Re-initializing scene1 so that mocked objects are stored
        # in their new state in the dictionary under __init__.
        self.scene1 = Scene1_CaveMouth(self.player, self.plot_points, self.fairy)
        try:
            self.scene1.enter()
        except SystemExit:
            self.assertEqual(mock_print.call_count, 2)
            mock_look.assert_called_once()
            mock_interact.assert_called_once()
            mock_talk.assert_called_once()
            mock_straw.assert_called_once()
            mock_fireball.assert_called_once()

    @patch("builtins.print")
    def test_interact(self, mock_print):
        self.scene1.action = "straw"
        self.scene1.player.mind.append("straw")
        self.scene1.interact_outcomes()
        mock_print.assert_called_with("\nYou pick up the prickly straw.")
        self.assertIn("straw", self.scene1.player.inventory)
        self.scene1.interact_outcomes()
        mock_print.assert_called_with("\nYou already took the straw.")

        action_values =         {
                                "mountain":"\nDidn't come here to climb the mountain, Mr Kong.",
                                "statue":"""The gods did not gift you with athleticism enough
                                        to climb the statues.""",
                                "bowl":"""If you had the spunk to climb the statues first,
                                        that wouldn't be out of the question.""",
                                "ivy":"""The ivies are silky to the touch. No practical use
                                    in taking one.""",
                                "door":"""Not the strongest men you've known would be able to budge
                                    it, and you're a munchkin compared to them."""
                                }

        for key in action_values:
            self.scene1.action = key
            self.scene1.interact_outcomes()
            mock_print.assert_called_with("\n" + action_values.get(key))
        
        self.scene1.action = "dud input"
        self.scene1.interact_outcomes()
        mock_print.assert_called_with("\nTrying to do that works. In your dreams.")

    @patch.object(Scene1_CaveMouth, "end_sequence")
    @patch("builtins.print")
    def test_straw(self, mock_print, mock_end):

        self.scene1.action = "dud input"
        self.scene1.straw_outcomes()
        mock_print.assert_called_with("\nYour attempt at action is beyond comprehension.")

        for word in ["bowl", "statue"]:
            self.scene1.player.inventory.append("straw")
            self.scene1.action = word
            self.scene1.straw_outcomes()
            mock_print.assert_called_with(textwrap.dedent("""
                                    You throw straw with all your might into
                                    both bowls atop the statue heads."""))
            self.assertNotIn("straw", self.scene1.player.inventory)
            self.assertIn("bowl of straw", self.scene1.environment)
            self.scene1.environment.remove("bowl of straw")
        
        self.scene1.action = "fireball"
        self.scene1.environment.append("bowl of straw")
        self.scene1.player.power.append("fireball")
        self.scene1.straw_outcomes()
        mock_end.assert_called()

        self.scene1.action = ""
        self.player.inventory.append("straw")
        self.scene1.straw_outcomes()
        mock_print.assert_called_with("\nNo use for the straw there.")

    @patch.object(Scene1_CaveMouth, "end_sequence")
    @patch("builtins.print")
    def test_fireball(self, mock_print, mock_end_sequence):
        """
        The fireball power leads to the end of the scene
        if aimed at the bowl while it has straw in it.
        """
        # A call that does not meet the conditions leads
        # to a cheeky message.
        self.scene1.fireball_outcomes()
        mock_print.assert_called_with("\nWaste of a good fireball.")

        self.scene1.player.power.append("fireball")
        self.scene1.environment.append("bowl of straw")
        # Check that, with the above conditions met,
        # the end sequence is called with either of the
        # below two strings contained in the user input.
        for i in ["bowl", "straw"]:
            self.scene1.action = i
            self.scene1.fireball_outcomes()
            mock_end_sequence.assert_called_once()
            mock_end_sequence.reset_mock()
    
    @patch.object(Scene2_CaveTunnel, "enter")
    def test_end(self, mock_enter_scene2):
        """
        The end_sequence function should call the next scene.
        """
        self.scene1.end_sequence()
        mock_enter_scene2.assert_called_once()
    
    @patch.object(Scene1_CaveMouth, "find_straw")
    @patch("builtins.print")
    def test_look(self, mock_print, mock_find_straw):
        self.scene1.action = "look"
        self.scene1.look_outcomes()
        mock_print.assert_called_with(textwrap.dedent("""
                                        ENTRANCE TO A CAVERN

                                        A cavern entrance towers in front of you. It is
                                        shut by a stone door.

                                        Stone statues flank it. They resemble warriors
                                        with spears and have bowls on their heads.

                                        Ivy creeps aside the mountain foot. The mountain
                                        is part of a range ascending into the cloudy
                                        distance.

                                        A fairy, materialised from thin air, floats and
                                        glowers about you."""))

        self.scene1.action = "statue"
        self.scene1.look_outcomes()
        mock_find_straw.assert_called_once()

        self.scene1.action = "straw"
        self.scene1.player.mind.append("straw")
        self.scene1.look_outcomes()
        mock_print.assert_called_with(textwrap.dedent("""
                                        Perhaps descendants of the tribals who lived here
                                        had use for straw in reigniting their tribal rituals."""))

        action_values =         {
                                "cavern":"""The cavern's rock formation reminisces
                                            of a scowling face, the entrance its maw.""",
                                "door":"""On the stone doors is a carving of a kraken with a
                                        thousand eyes, sticking out its tentacles from a dark
                                        pit. Must be Lullazilla.""",
                                "mountain":"""Red rivers run down the distant mountainsides
                                            like arteries on the body of a sleeping stone giant.""",
                                "ivy":"""Something about looking at a flower brings about the
                                        eternal in a person. And something about trying to be
                                        poetic reminds you your family couldn't afford schooling.""",
                                "fairy":"\nShe nonchanalantly hovers about."
                                }

        for key in action_values:
            self.scene1.action = key
            self.scene1.look_outcomes()
            mock_print.assert_called_with(textwrap.dedent("\n" + action_values.get(key)))
        
        self.scene1.action = "dud input"
        self.scene1.look_outcomes()
        mock_print.assert_called_with(textwrap.dedent("\nNot much to see."))

    @patch.object(Metacy, "start_dialogue")
    @patch("builtins.print")
    def test_talk(self, mock_print, mock_start_dialogue):

        for word in ["fairy", "metacy"]:
            self.scene1.action = word
            self.scene1.talk_outcomes()
            mock_start_dialogue.assert_called_once()
            mock_start_dialogue.reset_mock()
        
        self.scene1.action = "straw"
        self.scene1.player.mind.append("straw")
        self.scene1.talk_outcomes()
        mock_print.assert_called_with(textwrap.dedent("""
                                        Contrary to bumpkin belief, straw doesn't make
                                        an excellent conversation partner."""))

        action_values =         {
                                "cavern":"""You know you're in your social element if you can
                                hold the interest of a rock formation.""",
                                "door":"\nSaying \"open sesame\" has no effect.",
                                "ivy":"The ivies say hi. Just kidding, dumbass.",
                                "mountain":"\nMountain didn't come here to make friends, either.",
                                "statue":"""Their deafness to your heartfelt soliloquys makes your
                                            skin crawl."""
                                }

        for key in action_values:
            self.scene1.action = key
            self.scene1.talk_outcomes()
            mock_print.assert_called_with(textwrap.dedent("\n" + action_values.get(key)))

        self.scene1.action = "dud input"
        self.scene1.talk_outcomes()
        mock_print.assert_called_with("\nCan't talk to inanimate objects or figments of your imagination.")

    @patch("builtins.print")
    def test_find_straw(self, mock_print):
        """
        If the player is not carrying the straw and the straw
        is not in the bowl, that means it's still behind the
        statue, so a message should print communicating that,
        and its existence should be added to the player's
        mind if it hasn't already been added. If either of
        those first two condition is untrue, it means
        the player has already taken the straw, so an
        appropriate message should print.
        """
        self.scene1.find_straw()
        self.assertIn("straw", self.scene1.player.mind)

        self.scene1.player.inventory = ["straw"]

        self.scene1.player.inventory = ["straw"]
        mock_print.reset_mock()
        self.scene1.find_straw()
        mock_print.assert_called_once()
        mock_print.reset_mock()
        self.scene1.player.inventory = []
        
        self.scene1.environment = ["bowl of straw"]
        self.scene1.find_straw()
        mock_print.assert_called_once()
