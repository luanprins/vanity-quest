from Universe.Scene import Scene
from Universe.Scene2_CaveTunnel import Scene2_CaveTunnel
import textwrap

class Scene1_CaveMouth(Scene):

    def __init__(self, player, plot_points):
        super().__init__(player, plot_points)
        self.extra_accepted_inputs = {
                                        "look":self.look_outcomes,
                                        "interact":self.interact_outcomes,
                                        "talk":self.talk_outcomes,
                                        "straw":self.straw_outcomes,
                                        "fireball":self.fireball_outcomes
                                        }

    def enter(self):
        while True:
            super().enter()

            for word in self.extra_accepted_inputs:
                if word in self.action:
                    self.extra_accepted_inputs.get(word)()
                    self.enter()

            print("\nTry a different input or type help.")

    def interact_outcomes(self):
        """
        If the player has noticed the straw they can add it to
        their inventory through this method.
        """
        # Interacting with these keys results in ambient quips.
        self.ambient_inputs = {
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

        if "straw" in self.action and "straw" in self.player.mind:
            if "straw" not in self.player.inventory:
                print("\nYou pick up the prickly straw.")
                return self.player.inventory.append("straw")
            # Here we make sure you can't pick up new straw if it's been
            # used to open the stone doors or if it's in the inventory.
            else:
                return print("\nYou already took the straw.")

        for word in self.ambient_inputs:
            if word in self.action:
                return print(textwrap.dedent(self.ambient_inputs.get(word)))
        
        return print("\nTrying to do that works. In your dreams.")

    def straw_outcomes(self):
        """
        If the player has straw, they can throw it into the bowls
        atop the statue heads. If they fireball it afterward, end
        sequence plays.
        """
        if "straw" in self.player.inventory and \
        ("bowl" in self.action or "statue" in self.action):
            print(textwrap.dedent("""
                                You throw straw with all your might into
                                both bowls atop the statue heads."""))
            self.player.inventory.remove("straw")
            self.environment.append("bowl of straw")
        elif "fireball" in self.action and "bowl of straw" in self.environment:
            self.end_sequence()
        else:
            print("\nNo use for the straw there.")

    def fireball_outcomes(self):
        """
        Attempting fireball runs a check to ensure it's learned.
        Then, if straw is already thrown in the bowls and they're
        targeted, the player moves to the next scene, else no cigar.
        """
        if "fireball" in self.player.power and \
        "bowl of straw" in self.environment and \
        ("bowl" in self.action or "straw" in self.action):
            self.end_sequence()
        else:
            print("\nWaste of a good fireball.")

    def end_sequence(self):
        print(textwrap.dedent("""
                    You set the ritual straw atop the spearmen's heads aflame!
                    Their eyes begin to burn in sync with their heads. You fear
                    they may awaken at any moment. The earth teems with tremours
                    as the stone doors shift open and you proceed inside."""))
        Scene2_CaveTunnel(self.player, self.plot_points).enter()

    def look_outcomes(self):
        """
        The player spots a bunch of straw behind a statue
        when they look at it. This gives them the ability
        to interact with it.
        """
        self.ambient_inputs = {
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

        # Converse to other actions, entering 'look' alone describes the environment.
        if self.action == "look":
            return print(textwrap.dedent("""
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
        elif "statue" in self.action:
            print(textwrap.dedent("""
                                Some detailed sculptures of fat warriors with pustuled
                                skin stare you down."""))
            # Runs a method that adds straw to your mind if not
            # already there, prints something, and returns.
            return self.find_straw()
        elif "straw" in self.action and "straw" in self.player.mind:
            return print(textwrap.dedent("""
                                        Perhaps descendants of the tribals who lived here
                                        had use for straw in reigniting their tribal rituals."""))

        for word in self.ambient_inputs:
            if word in self.action:
                return print(textwrap.dedent(self.ambient_inputs.get(word)))

        return print(textwrap.dedent("\nNot much to see."))

    def talk_outcomes(self):
        """
        The player can talk to Metacy to run the method that gets them
        the fireball, or they can talk with inanimate objects in vain.
        """
        self.ambient_inputs = {
                                "cavern":"""You know you're in your social element if you can
                                hold the interest of a rock formation.""",
                                "door":"\nSaying \"open sesame\" has no effect.",
                                "ivy":"The ivies say hi. Just kidding, dumbass.",
                                "mountain":"\nMountain didn't come here to make friends, either.",
                                "statue":"""Their deafness to your heartfelt soliloquys makes your
                                            skin crawl."""
                                }

        # Talking to metacy can get you the fireball
        # which is part of the solution.
        if "fairy" in self.action or "metacy" in self.action:
            return self.metacy_mouth()
        elif "straw" in self.action and "straw" in self.player.mind:
            return print(textwrap.dedent("""
                                        Contrary to bumpkin belief, straw doesn't make
                                        an excellent conversation partner."""))

        for word in self.ambient_inputs:
            if word in self.action:
                return print(textwrap.dedent("\n" + self.ambient_inputs.get(word)))

        return print("\nCan't talk to inanimate objects or figments of your imagination.")

    def find_straw(self):
        """
        After seeing the straw this method adds it to
        your character's mind if it isn't there already.
        If you've already picked it up, this method lets
        you know that there's vacuousness where straw once
        was.
        """
        if "straw" not in self.player.inventory and "bowl of straw" not in self.environment:
            print("\nSomeone left some straw behind one statue.")
            if "straw" not in self.player.mind:
                self.player.mind.append("straw")
        else:
            print("\nThere is vacuousness where straw once was.")

    def metacy_mouth(self):
        """
        The player can listen to some lore here and needs
        the fireball grant to advance.
        """
        print(textwrap.dedent("""
                                The fairy regards you with glowing ember eyes.
                                Input the corresponding number for dialogue."""))

        while True:

            print("1. Who are you?")

            if "metacy visible" in self.player.mind:
                print("\n2. How come only I can see you?")
            else:
                print(textwrap.dedent("""
                                    2. <Option locked – you haven't found out her
                                    usual appearance.>"""))

            if "metacy butts" in self.player.mind:
                print(textwrap.dedent("""
                                    3. You really burn butts when you're invisible?"""))
            else:
                print(textwrap.dedent("""
                                    3. <Option locked – your butt knowledge is not
                                    sufficient.>"""))

            if "metacy soulmate" in self.player.mind:
                print(textwrap.dedent("""
                                    4. You mentioned our souls were split – are we
                                    soulmates?"""))
            else:
                print(textwrap.dedent("""
                                    4. <Option locked – you don't know the truth
                                    about your soul.>"""))

            if "fireball" not in self.player.power:
                print(textwrap.dedent("""
                                    5. How do I get into the cave?"""))
            else:
                print(textwrap.dedent("""
                                    5. <Option terminated – you've already learned
                                    the fireball spell.>"""))

            print("""\n6. Thanks for the chat.""")

            # Input to choose from the above list of dialogue options.
            talk_metacy = input("\n> ")

            if talk_metacy == "1":
                print(textwrap.dedent("""
                                    'I am Metacy,' she says. 'I've lived here for generations
                                    because my energy is that of fiery passion, and here fire is the
                                    ruling force aside from dreams. Strange: most humans can't see me,
                                    but you can. How am I supposed to burn your butt without getting
                                    caught now?' """))
                self.player.mind.append("metacy visible")
                self.player.mind.append("metacy butts")
            elif talk_metacy == "2" and "metacy visible" in self.player.mind:
                print(textwrap.dedent("""
                                    'Legends say that if a human can see a fairy their two
                                    souls were one and the same in a past life. If I can
                                    help you achieve your purpose I may sever my ties to this
                                    old hothole. No chance I'm being selfless for my own gain,
                                    right?' """))
                self.player.mind.append("metacy soulmate")
            elif talk_metacy == "3" and "metacy butts" in self.player.mind:
                print(textwrap.dedent("""
                                    Metacy says, 'if you'd been bound for centuries to a
                                    sanitarium of stone, and your corporal needs and
                                    desires were void, could you come up with a better
                                    entertainment form than sizzling passing adventurer arse?"""))
            elif talk_metacy == "4" and "metacy soulmate" in self.player.mind:
                print(textwrap.dedent("""
                                    'Of a sort,' she says.

                                    But your gaze doesn't falter – you must know whether your quest
                                    to avenge the noble Beth is vain or not. If this is your soulmate,
                                    why on Apeiron are you trying to impress some living woman?

                                    'Who am I fooling,' continues Metacy. 'We are soulmates. There is no
                                    doubt about it. But humans romanticise things. Being soulmates doesn't
                                    mean we have to, you know.'

                                    Metacy pauses, a distant look in her eyes.

                                    She clears her throat; '"Soulmates" means our souls are destined to
                                    merge again in the end. It may be several lifetimes from now. But
                                    our connection to each other won't fade, and our paths may overlap
                                    multiple times, in different forms, until then.'

                                    'Besides,' comes her afterthought, 'humans and fairies can't be
                                    physical, except through magic."""))
                self.player.mind.append("metacy magic")
            elif talk_metacy == "5" and "fireball" not in self.player.power:
                print(textwrap.dedent("""
                                    'I can't interact with the physical world but I can make
                                    certain things materialise in the physical world.

                                    'Because you are my soulmate, you can magnify the power of these
                                    manifestations.

                                    'Because my soul essence is raging hot fervour, I can bestow the
                                    power to cast a fireball. Close your eyes . . .'

                                    You obey Metacy's command and soon feel a piercing hot flash thunder
                                    through your skull. It is the worst pain you've experienced, however
                                    it's over in a matter of seconds.

                                    The air feels fresher when next you draw breath.

                                    'You are here to slay Lullazilla,' says Metacy. 'I have never braved its
                                    cave, but I know how to open it. The flames atop both flanking spearman
                                    statues must burn.' """))
                self.player.power.append("fireball")
            elif talk_metacy == "6":
                print("\n'Pleasure,' says Metacy.")
                return
            else:
                print("\nPlease enter only a valid number.")

        return
