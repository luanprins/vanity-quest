# Gets a class with mind, inventory, and world lists.
# Player choice updates the lists which are checked to progress.
from Characters import PlayerCharacter
# Gets scenes which return following scenes as strings.
import Universe.Scene1_CaveMouth
import Universe.Scene2_CaveTunnel
import Universe.Scene3_InsideCave
import Universe.Scene4_CrystalRoom
# Multiline strings get dedented with the textwrap module.
import textwrap

class Engine():
    """
    Takes returns from scenes and feeds them to the map,
    which returns matching instances of the new scenes, which
    are then run by the engine."""

    def __init__(self, player):
        self.scenes = {
                    "scene1":Universe.Scene1_CaveMouth.Scene1_CaveMouth(player),
                    "scene2":Universe.Scene2_CaveTunnel.Scene2_CaveTunnel(player),
                    "scene3":Universe.Scene3_InsideCave.Scene3_InsideCave(player),
                    "scene4":Universe.Scene4_CrystalRoom.Scene4_CrystalRoom(player),
                    "endgame":"<placeholder for endgame class>"
                    }

    def run(self):

        # Game begins with a message.
        print(textwrap.dedent("""
                            Welcome to Vanity Quest. Your totally meaningful
                            journey awaits.

                            Type "help" for info on how to play.
                            Type "load" to resume a previous game.
                            Type "exit" to terminate the game."""))

        current_scene = self.scenes.get("scene1")

        while current_scene != self.scenes.get("endgame"):
            # Every scene ends by returning a string named after the next scene.
            current_scene = self.scenes.get(current_scene.enter())
        # When the loop breaks, the final scene runs.
        current_scene.enter()

player = PlayerCharacter.PlayerCharacter()
the_engine = Engine(player)
the_engine.run()
