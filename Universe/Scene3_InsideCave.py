from Universe.Scene import Scene
from Universe.Scene4_CrystalRoom import Scene4_CrystalRoom
import textwrap

class Scene3_InsideCave(Scene):

    def enter(self):

        while True:
            super().enter()

            if "talk" in self.action and ("fairy" in self.action or "metacy" in self.action):
                self.scene3_metacy()
            elif "look" in self.action:
                self.look_outcomes()
            elif "fireball" in self.action:
                self.fireball_outcomes()
            elif "interact" in self.action:
                self.interact_outcomes()
            # The spike needs to be shaped into a hook using lava.
            elif "spike" in self.action and "spike" in self.player.inventory:
                self.spike_outcomes()
            # You attach the hook to the rope.
            elif "hook" in self.action and "hook" in self.player.inventory:
                self.hook_outcomes()
            # You use the grapple rope on the stalagmite and fallen stalactite to advance.
            elif any(x in self.action for x in ["rope", "hook", "grapple rope"]) \
                and "grapple rope" in self.player.inventory:
                self.grapple_outcomes()
            else:
                print("\nYou're speaking tongues.")

    def interact_outcomes(self):
        if "river" in self.action:
            print("\nYou didn't bring your swimwear. Or a coffin.")
        elif "stalagmite" in self.action:
            print("\nCan't jump all the way.")
        elif "stalactite" in self.action:
            print("\nThe Gods didn't bless you with that kind of length.")
        # Get rope and spike this way.
        elif "rope" in self.action and "rope" not in self.player.inventory:
            print("\nGot the rope.")
            self.player.inventory.append("rope")
        elif "spike" in self.action:
            print("\nGot the spike.")
            self.player.inventory.append("spike")
        # Long boolean so the lava pool on the platform can be referred to as
        # 'lava' or as 'pool' but excluding 'lava river' or 'river of lava'.
        elif "pool" in self.action or ("lava" in self.action and "river" not in self.action):
            print(textwrap.dedent("""
                                You almost dip your hand in there. Then you realise it's your crazy side doing
                                the thinking."""))
        elif "orb" in self.action and "fallen stalactite" not in self.environment:
            print(textwrap.dedent("""
                                You bitch-slap the orb and it boings back to its
                                original erect position, unperturbed."""))
        else:
            print("\nPlease suck less.")

    def fireball_outcomes(self):
        if "rope" in self.action:
                    print("\nSeems impractical to burn a good rope.""")
        elif "spike" in self.action:
            print(textwrap.dedent("""
                                Fireball hits the spike but it doesn't ignite and the magical projectile disperses
                                before even heating the steel thoroughly."""))
        elif "orb" in self.action and "fallen stalactite" not in self.environment:
            # Here you drop the stalactite on your side.
            print(textwrap.dedent("""
                                The orb promptly recedes into the narrow crevice it stuck out from. Then
                                a guttural sound resonates from the depths, lower than the oldest whale's
                                call and louder than a drunk wench's love-forlorn shrieks. The world vibrates
                                and you almost lose your footing even as you cover your ears. Metacy grabs your
                                arm and points up. You follow her indication and dread fills your eyes. You jump
                                out of the way just in time for your skull not be impaled by the falling stalactite,
                                which roots itself upright in the soft plot of ground underneath it, just by the
                                edge separating the platform from a long drop into the river of lava below."""))
            self.environment.append("fallen stalactite")
            print(textwrap.dedent("""
                                'You saved my life,' you murmur.

                                'So did you mine, in some past life,' says Metacy. She seems ponderous for a moment
                                before adding, 'Probably.' """))
        else:
            print("\nIt's hot enough already.")

    def grapple_outcomes(self):
        if ("stalagmite" in self.action or "stalactite" in self.action) and "fallen stalactite" in self.environment:
            print(textwrap.dedent("""
                                You epically throw the hook end of the rope at the narrowest stalagmite on the other side of the river.
                                You pull it taut, making sure the hook caught. Then you tie the other end of the rope around the fallen
                                stalactite. You hug the rope and slowly climb over the boiling, fatal current below, heart pounding.
                                Landing on the other side, you release a sigh of relief.

                                You pass through a tunnel to the next room."""))
            self.player.inventory.remove("grapple rope")
            Scene4_CrystalRoom(self.player, self.plot_points, self.fairy).enter()

    def hook_outcomes(self):
        if "rope" in self.action:
            print("\nYou attach the rope to the hook, tying it tightly. Good as makeshift grapple ropes come!""")
            self.player.inventory.remove("hook")
            self.player.inventory.append("grapple rope")
            if "rope" in self.player.inventory:
                self.player.inventory.remove("rope")
        else:
            print("\nNo use for it there.")

    def look_outcomes(self):
        if self.action == "look":
            print(textwrap.dedent("""
                                INSIDE THE CAVE

                                The air is rippling with the heat emanating from the
                                lava river.

                                There are stalagmites on the other side of the river.
                                That platform is a good deal lower than here. There are
                                no stalagmites among you but stalactites dangle precariously
                                from the ceiling.

                                Some rope lies rolled up a few paces away from you.
                                Next to it is a large steel spike.

                                One end of the river is so infernal that
                                bouts of lava shoot into the air and form a small pool
                                on your side of the hellish stream.

                                A strange blue orb protrudes from the ground in the centre
                                of this clearing.
                                """))
            self.player.mind.append("orb")
        # Rest of the looks serve no functional purpose for this scene.
        elif "river" in self.action:
            print("\nYou pray to the gods you don't end up in there.")
        elif "stalagmite" in self.action:
            print("\nNothing phallic about them whatsoever.")
        elif "stalactite" in self.action:
            print(textwrap.dedent("""
                                You had trouble remembering what they're called, until you
                                realised the latter syllable sounded similar to another hanging
                                marvel of nature."""))
        elif "rope" in self.action:
            print("\nLooks like it wouldn't snap if something heavy hung from it.")
        elif "spike" in self.action:
            print(textwrap.dedent("""
                                Guess you might stab something to death with it, but
                                reassembling the sword and THEN killing in cold blood
                                seems far more heroic."""))
        elif "pool" in self.action or ("lava" in self.action and "river" not in self.action):
            print("\nYou don't want to touch it – would probably deform your very bones.")
        elif "orb" in self.action and "fallen stalactite" not in self.environment:
            print("\nYou don't want to know, but something tells you you don't have a choice.")

    def spike_outcomes(self):
        """
        The desired outcome of this method is for the player
        to shape the spike into a hook by dipping it into
        lava.
        """

        if "pool" in self.action or ("lava" in self.action and "river" not in self.action):
            print("\nYou dip the spike in the pool of lava and bend it to form a hook.")
            self.player.inventory.remove("spike")
            self.player.inventory.append("hook")

        # Other outcomes are a process of elimination.
        elif "orb" in self.action and "fallen stalactite" not in self.environment:
            print(textwrap.dedent("""
                                You attempt to stab it to no avail: it bends away from the pointy end rather than
                                being impaled."""))
        elif "rope" in self.action:
            print(textwrap.dedent("""
                                Hmmm, a rope with a straight spike attached to it? Not quite the customary climbing
                                requisite."""))
        else:
            print("\nNo use for it there.")

    def scene3_metacy(self):

        print(textwrap.dedent("""
                            Metacy beams, probably at the thought of your continued
                            survival, which seemed so against all odds ever."""))

        if "healer" in self.environment:
            print("\n1. The healer couldn't see you but was able to draw power from you. Why?""")
        else:
            print("\n1. What was that blue stream you healed me with?""")

        print(textwrap.dedent(""""
                            2. Gorgols – what are they?

                            3. Know anything about this broken sword?

                            4. Alright, back to work."""))

        if "orb" in self.player.mind.append("orb"):
            print("\n5. Care to explain the strange blue protruberance?")
        else:
            print("\n5. <option locked – you haven't looked around yet.")

        while True:

            scene3_metacy_act = input("\n> ")

            if scene3_metacy_act == "1" and "healer" in self.environment:
                print(textwrap.dedent("""
                                    'Healers have a limited supply of mana. With every spell it's reduced.
                                    To regenerate it, they have to draw directly from the Uncanny Plane,
                                    or from something that has passed into the physical world from it.

                                    'The uncanny plane is among people. Fairies frolick and go about their
                                    festivities on the same lands that people do, but unbeknownst to them.
                                    There are also crystals and growths containing mana. These things, healers
                                    can see. But not fairies. So in their ignorance they refer to us as 'magical
                                    auras' and draw the energy from us if they're near.

                                    'Luckily they can't draw enough from us to make us disappear.' """))
            elif scene3_metacy_act == "1":
                print(textwrap.dedent("""
                                    'That was mana. It is the lifeblood of most things that exist in the
                                    Uncanny Plane, a world among yours. Fairies go about their days
                                    on the same lands people do, unbeknwonst to them, making music and
                                    living a life that is much less bent on violence and insanity, and
                                    more concerned with maintaining the beauty and purity of all things
                                    within their reach. It is this way of being that unlocks the mana
                                    within them.

                                    'Healers like the one who passed away here refer to us as 'magical
                                    auras' because we are not visible to them and so most of them don't
                                    believe that the creatures who are their main source of power even
                                    exist. Luckily, they can't draw enough from us to kill us. And they
                                    can see things like crystals and growths from the Uncanny Plane from
                                    which they also draw their mana.' """))
            elif scene3_metacy_act == "2":
                print(textwrap.dedent("""
                                    'Digusting, aren't they? You might not believe my answer – it is not
                                    commonly known among humans, but we fairies have a longer lifespan
                                    and so many of us have seen what you call ancient history with our
                                    very own eyes. Too bad most humans can't see fairies and the ones
                                    who are in the minority are too few and far between for their ideas
                                    to be regarded as more than mere crazy ramblings.

                                    'The gorgols are the last people of the Hade tribe. So, if you believe
                                    being stripped of your humanity isn't the equivalent of dying, they
                                    aren't technically wiped away.

                                    'The Hade people worshipped Lullazilla and from his maw came vapours
                                    which they captured and turned into a poison with which they hunted
                                    animals. This was the instruction of the Dreamers; elder tribal leaders
                                    who laid their hands on the hide of Lullazilla to gain visions for
                                    guidance and in doing so lost their real-world eyesight. The poison
                                    ensured even the largest wild beast would die with a single arrow.
                                    But there was also a drawback to eating their flesh – one which took
                                    years to show its full effect, by which time most of the tribe
                                    had already partaken of the meat that would turn them into gorgols.' """))
            elif scene3_metacy_act == "3":
                print(textwrap.dedent("""
                                    Metacy studies the pommel carefully – a shimmering and candied-looking
                                    ruby.

                                    'There's no doubt about it,' she says. 'That's the Blade of Consciousness.'

                                    'The blade of what?' you say.

                                    'Counsciousness. As in, not oblivion, slumber, ignorance – all those
                                    closed-minded things. It was crafted by the smith of a legendary warrior
                                    Pithox who sought to kill Lullazilla hundreds of years ago when the Hade
                                    tribe took one of their children to offer as sustenance to the great
                                    and terrible maw of their demigod.

                                    'The Hade people were fierce – but they knew fear. The
                                    exploits of Pithox had gained fame even in their subterranean tongue.
                                    When he came down here, they hid away. But when he came to the slumber
                                    hollow of Lullazilla, and made to strike, it caught him with a tentacle,
                                    sending him flying and crashing into a plume of blood, his sword scattered
                                    into three pieces.

                                    'The Hade people knew the threat that the blade posed, for one thing.
                                    And for another, they reveled in having a memento of such a valiant
                                    attempt to end the source of their piety. So – they took two pieces
                                    of the blade and hid it in the deepest and most unreachable reaches of
                                    this cavern's awfully perplexing tunnel system. To make sure that the
                                    blade wouldn't be repaired, they sent their slyest rogue away to hide
                                    it – none but the rogue knew its location, and all swore an oath
                                    never to speak of his embarkation, for fear that information of it
                                    might later be forced out of him.'

                                    'So there is no way to repair the blade?' you say.

                                    'There is. You have a fairy on your side. Simply find the first two
                                    pieces and through the power of metal magic I shall forge the rest.' """))
            elif scene3_metacy_act == "4":
                print("\n'I'm right here with you,' says Metacy.")
                return
            elif scene3_metacy_act == "5":
                print(textwrap.dedent("""
                                    For as long as the dreaded demigod has his minions, he continues to grow
                                    in size. There is a very deep vacuum underneath him, but his vessel is pliable
                                    as the matter of dreams, so much of him has expanded through narrow crevices
                                    and stick out in parts of the cave quite some distance from his sleeping chamber."""))
