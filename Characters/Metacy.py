from Characters.NPC import NPC
import textwrap

class Metacy(NPC):

    def __init__(self):
        super().__init__()
        self.intro_lines = [
                            "\nThe fairy awaits your concern with a playful grin.",
                            "\n\"How can I help, human?\"",
                            "\nMetacy regards you with still patience and a prompting gaze."
                            ]
        self.greetings = [
                        "\n\"Regards, my friend.\"",
                        "\n\"Watch your back.\"",
                        "\n\"Take care.\"",
                        "\n\"I'm right aside you.\"",
                        "\n\"All ears if you need me.\""
                        ]
        self.place_dependent_topics = {
                                # Latter list item for scene 1 will change so that Metacy's response depends on whether
                                # the player has learned the fireball.
                                "scene1":{
                                        "Who are you?":
                                        self.s1_introduce,
                                        "How do I get into the cave?":
                                        self.s1_fireball_grant
                                        },
                                }
        self.player_dependent_topics = {
                                        "scene1":{
                                                "metacy visible":{
                                                                "player line":
                                                                "How come only I can see you?",
                                                                "response":
                                                                self.s1_soulmate_lore
                                                                },
                                                "metacy butts":{
                                                                "player line":
                                                                "You really burn butts when you're invisible?",
                                                                "response":
                                                                self.s1_butt_lore
                                                                },
                                                "metacy soulmate":{
                                                                "player line":
                                                                "You mentioned our souls were split – are we soulmates?",
                                                                "response":
                                                                self.s1_soulmate_reveal
                                                                }
                                                }
                                        }

    def s1_fireball_grant(self, player):
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
        player.power.append("fireball")
    def s1_introduce(self, player):
        print(textwrap.dedent("""
                            'I am Metacy,' she says. 'I've lived here for generations
                            because my energy is that of fiery passion, and here fire is the
                            ruling force aside from dreams. Strange: most humans can't see me,
                            but you can. How am I supposed to burn your butt without getting
                            caught now?' """))
        player.mind.append("metacy visible")
        player.mind.append("metacy butts")

    def s1_soulmate_lore(self, player):
        print(textwrap.dedent("""
                            'Legends say that if a human can see a fairy their two
                            souls were one and the same in a past life. If I can
                            help you achieve your purpose I may sever my ties to this
                            old hothole. No chance I'm being selfless for my own gain,
                            right?' """))
        player.mind.append("metacy soulmate")

    def s1_soulmate_reveal(self, player):
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
        player.mind.append("metacy magic")

    def s1_butt_lore(self, player):
        print(textwrap.dedent("""
                            Metacy says, 'if you'd been bound for centuries to a
                            sanitarium of stone, and your corporal needs and
                            desires were void, could you come up with a better
                            entertainment form than sizzling passing adventurer arse?"""))
