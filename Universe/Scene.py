import pickle
import textwrap

class Scene():
    # player = PlayerCharacter()
    plot_points = []

    def __init__(self, player, plot_points):
        # Keeps track of how the environment changes in every scene.
        self.environment = []
        self.player = player
        self.plot_points = plot_points

    def enter(self):
        """
        The enter method for all scenes takes an input. The
        super().enter() method gets called in each child class's
        version, which continues with its own checks on the input.
        """

        self.action = input("\n> ")
        if self.action == "environment":
            self.enter()
        elif self.action == "help":
            self.help_method(self.environment)
            self.enter()
        elif self.action == "inventory":
            self.player.show_inventory()
            self.enter()
        elif self.action == "save":
            self.save_game()
            self.enter()
        elif self.action == "load":
            self = self.load_game()
            self.enter()
        elif self.action == "exit":
            print("\nUntil next time.")
            exit()
        else:
            pass

    def help_method(self, environment):
        """
        New players use this to familiarise themselves with the game.
        """

        print("\nNever fear: help is here. Type the number you need.")

        while True:
            print(textwrap.dedent("""
                                1. Who am I?
                                2. How do I control myself?
                                3. Back to game.
                                """))
            help_act = input("\n> ")
            if help_act == "1":
                print(textwrap.dedent("""
                                    You are Barthol, the mercenary of Cyaton, a small apple
                                    farming village nearby Moat Serene City, over which the
                                    the bard-come-baron Gallafast rules with a hairy fist.

                                    You have promised to slay the sleeping demigod Lullazilla
                                    to prove that you can slay greater monsters than the man
                                    who inappropriately groped Lady Beth, Gallafast's noble
                                    daughter.

                                    How . . . vain."""))
            elif help_act == "2":
                print(textwrap.dedent("""
                                    You have skills that get added to throughout the game.
                                    To use them, simply type them. At the start, they are:

                                    look – type 'look' to see what's going on around you, or
                                    combine it with an object (for example 'look statue') to
                                    focus on something in particular.

                                    interact – combine with something in the environment to
                                    interact with it, for example, 'interact ladder' would translate
                                    to climbing a ladder, 'interact bed' would translate to sleeping
                                    on it . . . think twice about big red buttons, though.

                                    talk – you don't exactly have a silver tongue, but you
                                    may be able to extract the information you need from people
                                    if they're gullible enough to like you."""))
                # There are a few checks here only to print instructions
                # for powers that are already unlocked.
                if "fireball" in self.player.power:
                    print(textwrap.dedent("""
                                        fireball – turn foes or obstacles into piles of dust with
                                        this elemental ability which exhibits the fiery nature of
                                        your fairy companion's soul in an immolative orchestration."""))
                else:
                    print(textwrap.dedent("""
                                        <Play more to unlock additional power 1>"""))
            elif help_act == "3":
                break
            else:
                print(textwrap.dedent("""
                                    The help guide's helpfulness is unfortunately limited to what
                                    it dictates."""))

    def save_game(self):

        print(f"Saving with self as {self} and player as {self.player}.")
        save_file = open("savegame.pickle", "wb")
        pickle.dump(self, save_file)
        save_file.close()
        print("Saved.")

    def load_game(self):

        load_file = open("savegame.pickle", "rb")
        loaded_content = pickle.load(load_file)
        load_file.close()
        return loaded_content
