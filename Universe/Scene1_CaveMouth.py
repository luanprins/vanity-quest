from Universe.Scene import Scene
from Universe.Scene2_CaveTunnel import Scene2_CaveTunnel
import textwrap

class Scene1_CaveMouth(Scene):

    def enter(self):
        while True:
            super().enter()

            if "look" in self.action:
                self.look_outcomes()
            elif "interact" in self.action:
                self.interact_outcomes()
            elif "talk" in self.action:
                self.talk_outcomes()
            # If they have straw, they can throw it into the bowls.
            elif "straw" in self.action and "straw" in self.player.inventory:
                if "bowl" in self.action or "statue" in self.action:
                    print(textwrap.dedent("""
                                        You throw straw with all your might into
                                        both bowls atop the statue heads."""))
                    self.player.inventory.remove("straw")
                    self.environment.append("bowl of straw")
                else:
                    print("\nNo use for the straw there.")
            # Attempting fireball runs a check to ensure it's learned.
            elif "fireball" in self.action and "fireball" in self.player.power:
                # After throwing straw in bowls, combining the 'fireball' input
                # with 'bowl' or 'straw' will finally open the stone doors.
                if "bowl of straw" in self.environment and "bowl" in self.action or "straw" in self.action:
                    print(textwrap.dedent("""
                                        The spearmen's eyes begin to burn in sync with their heads.
                                        You fear they may awaken at any moment. The earth teems with
                                        tremours as the stone doors shift slowly open."""))
                    self.environment.append("door open")
                    # End value return is here. The name of the next scene gets fed back to the engine.
                    Scene2_CaveTunnel(self.player, self.plot_points).enter()
                else:
                    print("\nWaste of a good fireball.")

            else:
                print("\nTry a different input or type help.")

    def interact_outcomes(self):
        # These activations are not the solution.
        if "mountain" in self.action:
            print(textwrap.dedent("\nDidn't come here to climb the mountain, Mr Kong."))
        elif "statue" in self.action:
            print(textwrap.dedent("""
                                The gods did not gift you with athleticism enough
                                to climb the statues."""))
        elif "bowl" in self.action:
            print(textwrap.dedent("""
                                If you had the spunk to climb the statues first,
                                that wouldn't be out of the equation."""))
        elif "ivy" in self.action:
            print(textwrap.dedent("""
                                The ivies are silky to the touch. No practical use
                                in taking one."""))
        # This activation is part of the solution, and you
        # need to have spotted the straw by looking at
        # the statue in order for it to work.
        elif "straw" in self.action and "straw" in self.player.mind:
            if "straw" not in self.player.inventory:
                print("\nYou pick up the prickly straw.")
                self.player.inventory.append("straw")
            # Here we make sure you can't pick up new straw if it's been
            # used to open the stone doors or if it's in the inventory.
            elif "door open" in self.environment or "straw" in self.player.inventory:
                print("\nYou already took the straw.")
        elif "door" in self.action:
            print(textwrap.dedent("""
                                Not the strongest men you've known would be able to budge it,
                                and you're a munchkin compared to them."""))
        else:
            print("\nWon't work in this universe.")

    def look_outcomes(self):

        if self.action == "look":
            print(textwrap.dedent("""
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
        elif "cavern" in self.action:
            print("\nThe cavern's rock formation reminisces of a scowling face, the entrance its maw.")
        elif "door" in self.action:
            print(textwrap.dedent("""On the stone doors is a carving of a kraken with a thousand eyes,
                                sticking out its tentacles from a dark pit. Must be Lullazilla."""))
        elif "mountain" in self.action:
            print(textwrap.dedent("""
                                Red rivers run down the distant mountainsides
                                like arteries on the body of a sleeping stone giant."""))
        elif "statue" in self.action:
            print(textwrap.dedent("""
                                Some detailed sculptures of fat warriors with pustuled skin
                                stare you down."""))
            # Runs a method that adds straw to your mind if not
            # already there, prints something, and returns.
            return self.find_straw()
        # The last conditional is there because the straw has ceased
        # to exist when the door is open.
        elif "straw" in self.action and "straw" in self.player.mind and "door open" not in self.environment:
            print(textwrap.dedent("""
                                Perhaps descendants of the tribals who lived here
                                had use for straw in reigniting their tribal rituals."""))
        elif "ivy" in self.action:
            print(textwrap.dedent("""
                                Something about looking at a flower brings about the
                                eternal in a person. And something about trying to be
                                poetic reminds you your family couldn't afford schooling
                                so it's best not to."""))
        # Entering only 'look' describes the environment.
        else:
            print(textwrap.dedent("\nNot much to see."))
        
        return

    def talk_outcomes(self):
        # Talking to metacy can get you the fireball
        # which is part of the solution.
        if "fairy" in self.action or "metacy" in self.action:
            self.metacy_mouth()
        # These options are not the solution.
        elif "cavern" in self.action:
            print(textwrap.dedent("""You know you're in your social element if you can
                                hold the interest of a stone wall."""))
        elif "door" in self.action:
            print("\nSaying 'open sesame' has no effect.")
        elif "ivy" in self.action:
            print(textwrap.dedent("\nThe ivies say hi. Just kidding, dumbass."))
        elif "mountain" in self.action:
            print(textwrap.dedent("""
                                Mountain doesn't seem to have come here to make any
                                friends, either."""))
        elif "statue" in self.action:
            print(textwrap.dedent("""
                                Their glassy gazes and deafness to your heartfelt
                                soliloquys make your skin crawl."""))
        elif "straw" in self.action and "straw" in self.player.mind:
            print(textwrap.dedent("""
                                Contrary to farm villager belief, straw doesn't make
                                such an excellent conversation partner."""))
        else:
            print("\nGod knows who or what you're trying to talk to.")

        return

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

        return

    def metacy_mouth(self):
        """Runs when talking to Metacy at the cave mouth.
        Mostly for interest, though you need the fireball grant
        from here to advance."""

        print(textwrap.dedent("""
                                The fairy regards you with glowering ember eyes.
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
