# Gets scenes which return following scenes as strings.
from Characters import PlayerCharacter
from Universe.Scene import Scene
from Universe.Scene1_CaveMouth import Scene1_CaveMouth
# Multiline strings get dedented with the textwrap module.
import pickle
import textwrap

class Engine():
    """Takes returns from scenes and feeds them to the map,
    which returns matching instances of the new scenes, which
    are then run by the engine."""

    def run(self):

        # Game begins with a message.
        print(textwrap.dedent("""
                            Welcome to Vanity Quest. Your totally meaningful
                            journey awaits."""))
        
        load_or_new = input("Load or new? > ")

        if load_or_new == "load":
            pickle_in = open("savegame.pickle", "rb")
            game_start = pickle.load(pickle_in)
            pickle_in.close()
            print("Game loaded.")
        else:
            print(textwrap.dedent("You've chose to start a new game. Type 'help' at any time\n\
                to learn how to play."))
            game_start = Scene1_CaveMouth(player, plot_points)

        game_start.enter()

player = PlayerCharacter.PlayerCharacter()
print(">>> Instance of Engine() created in main scope.")
plot_points = []
game = Engine()
print(">>> running instance of Engine()")
game.run()
