from Characters.PlayerCharacter import PlayerCharacter # a class that represents you
from Characters.Metacy import Metacy # a class that represents your fairy companion
from Universe.Scene1_CaveMouth import Scene1_CaveMouth # a child class of Scene
import textwrap

print(textwrap.dedent("""
                    Welcome to Vanity Quest. Your totally meaningful
                    journey awaits. Newcomers type 'help'."""))

fairy = Metacy()
player = PlayerCharacter() # state changes throughout game
plot_points = [] # accumulates throughout scenes
Scene1_CaveMouth(player, plot_points, fairy).enter() # each scene ends with the same call of the next scene
