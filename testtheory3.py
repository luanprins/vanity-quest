from textwrap import dedent
import pickle

class Player():
    def __init__(self):
        self.inventory = []

class Room():
    
    def __init__(self, player):
        self.player = player

    def enter(self):
        while True:
            action = input(dedent("""Choose something to do:
                        1. Pick up a rock.
                        2. Check your pockets.
                        3. Save game.
                        4. Load game.
                        5. Exit.
                        >>>"""))

            if action == "1":
                print("You put the rock in your pocket.")
                self.player.inventory.append("rock")
            elif action == "2":
                print("Here's what you're carrying:")
                print(self.player.inventory)
            elif action == "3":
                save_file = open("something.pickle","wb")
                pickle.dump(self, save_file)
                save_file.close()
                print("Saved.")
            elif action == "4":
                load_file = open("something.pickle", "rb")
                self = pickle.load(load_file)
                load_file.close()
                print("Loaded.")
            elif action == "5":
                print("Goodbye.")
                quit()

player = Player()
room = Room(player)

room.enter()