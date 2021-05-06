from Universe.Scene import Scene
from Universe.Scene3_InsideCave import Scene3_InsideCave
import textwrap

class Scene2_CaveTunnel(Scene):

    def enter(self):
        print(textwrap.dedent("""
                            Inside the cave you descend a deep, narrow, rocky tunnel and your
                            ability to breathe properly diminishes with the increased air
                            pressure.

                            Soon you are heaving and pouring sweat. Who knew turning
                            into an adventurer would be so grimy?

                            'You don't look well,' says Metacy. 'The Hade tribe were so con-
                            ditioned to living in these underground systems that they're largely
                            believed to have evolved into a species different from human.'

                            She observes before continuing.

                            'I can cast a healing boon which will ease your state in the coming
                            chambers, though I won't be able to heal again for a while. Keep in
                            mind, your fireball is more effective the more energy you have.'

                            Not knowing the twists and turns that lie ahead, yet knowing the
                            many curveballs thrown at adventurers chronicled in your child-
                            hood bedtime stories, you know to choose your answer carefully.

                            1. 'I'm struggling but it won't kill me – keep your energy for
                            something more important.'

                            2. 'Best be sure – hit me with a healing spell.' """))
        while True:
            super().enter()
            if self.action == "1":
                self.choice1()
                break
            elif self.action == "2":
                self.choice2()
                break
            else:
                print("Not a valid choice.")
                continue
        
        next_scene = Scene3_InsideCave(self.player, self.plot_points)
        next_scene.enter()

# This choice will get your family ring stolen and save
# the life of a renowned healer. You'll get the
# first shard of the sword with which to kill Lullazilla.
    def choice1(self):

        print(textwrap.dedent("""
                            You muscle through the incrementing discomfort.

                            Then you reach a massive room that would surely echo your
                            voice if you deemed sparing the breath for it worthwhile.

                            You are on a plateau surrounded by a river of lava coming from
                            a crack in the upper left wall.

                            Suddenly from beyond the precipice jumps a swarm of small, green
                            creatures with spears and dreadlocks.

                            'Oh, Gods,' says Metacy. 'Gorgols!'

                            They set their devilish red eyes on you without missing a beat,
                            and charge at you with their spears.

                            'Fireball them!' says Metacy.

                            From your fingers arise the most pathetic wisps of smoke you've
                            ever witnessed, rather contradictory to what you expected out of
                            your career change from apple farmer's son.

                            The Gorgols swarm you until a dozen of them covers you completely,
                            pounding fists on your flesh and ripping out bunches of hair.

                            After bruising you notably, they search your immobile, semi-unconscious
                            body for valuables, and make off with a pouch of coppers and
                            your prized silver emerald ring passed down to you by your grandfather.

                            <Input anything to continue>"""))

        input("\n> ")

        print(textwrap.dedent("""
                            You stand up wincing in pain.

                            'I'm glad you're okay,' says Metacy. 'My fireballs aren't powerful
                            enough on their own to incapacitate even a single gorgol. Only to
                            manage a less severe mischief than is the mark of their endeavours.'

                            And for the first time, you notice that you weren't the only one the
                            gorgols left bruised and beaten.

                            'Who could that be?' you say.

                            'Someone who needs help,' says Metacy.

                            On a bed of rocks on the far end of the room lies an elder woman
                            barely moving apart from breathing. You run to her side and as you
                            draw near notice the Mark of the Healer on her hand.

                            Magic healers are rare and therefore typically prized members of the
                            nobility and royal courts. But she does not have the energy left to
                            heal herself.

                            Her eyes dart to you, then to Metacy, though she does not so much look
                            'at' the fairy as 'through' her, for the fairy is visible to none but you.

                            This does not seem to stop the healer from reaching out, muttering a phrase
                            under her breath, and pulling a blue stream of energy into her body, the
                            source none other than your preternatural companion.

                            The colour returns to her face and soon she is standing.

                            'You carry a magical aura with you,' she says. 'If not for you,
                            I would have passed away for sure.'

                            'Please take this with my gratitude,' she continues. She hands you
                            the hilt end of a sword, a shard of its blade still protruding atop.
                            'I came here to slay the beast you seek, for it devoured my lover
                            into its world of eternal slumber, and I sought vengeance. But that
                            godforsaken gorgol attack made me realise something: I'm a healer, not
                            an adventurer.'

                            As a last gesture of thankfulness, she places a palm on your forehead,
                            and fills you with newfound vigour that lifts the worst of your
                            physical ailments.

                            And with that, she sets off."""))
        self.plot_points.append("healer")
        self.player.inventory.remove("heirloom ring")
        self.player.inventory.append("shard 1")

    # This choice will spare your family ring and cause the healer to pass
    # away. You'll also get the first shard of the sword with
    # which to kill Lullazilla.
    def choice2(self):


        print(textwrap.dedent("""
                            Metacy unleashes a blue stream of energy from her whole
                            being into your body.

                            You tread the rest of the tunnel with enough energy to put
                            a bounce in your step and a spark about you.

                            You reach a plateau surrounded by a river of lava coming from
                            a crack in the upper left wall.

                            It's in a room of tremendous size and you let out a joyous
                            howl, listening to the echoes, content with your career
                            change from apple farmer's lazy son to adventuring hero!

                            Then, as if reading your thoughts, a rowdy horde of little
                            green men with dreadlocks and spears emerges from beyond the
                            precipice, red eyes locked on you and sprinting your way.

                            'Fireball them!' shouts Metacy.

                            You summon the power and unleash the fireball, sending the
                            poor buggers flying and burning, some falling on the stone
                            floor as charred husks of what they once were, others falling
                            in the river of lava in which their death by heat is redoubled.

                            One of them got near enough almost to snag your coin pouch,
                            another your prized silver emerald ring passed down to you by
                            your grandfather.

                            <Input anything to continue>"""))

        input("\n> ")

        print(textwrap.dedent("""
                            'That was close,' says Metacy. 'Even if I had kept my power,
                            my version of the fireball is more for mischief than causing
                            death.'

                            'Not everyone is so lucky, it seems,' you say, pointing across
                            the room.

                            Metacy's ember eyes follow your gesture to the elder woman lying
                            on a bed of rocks, rarely moving a mote except for when breathing.

                            'She needs help,' says Metacy.

                            You rush to the woman's side to see if you can be of aid. You notice
                            she has the Mark of the Healer on her hand; the sign of the one-in-a-
                            million magic healers who typically serve royal courts and nobility
                            only or become mad hermits renouncing any association with the despicable
                            lives the people they aid choose to lead.

                            'You,' says the healer with some difficulty, 'have a magical vibration
                            about you. I could just reach out and save myself from dying, but alas,
                            I don't think it'll happen . . . the energy is faded, as if used recently.

                            'I came here,' she continues, 'to slay Lullazilla after swallowing
                            my lover into its inner world of eternal slumber. Now it seems I am
                            to suffer a similar fate. You are here to do the same, aren't you?
                            Then take this.'

                            She removes from her bag the hilt of a sword with a shard of its blade
                            still protruding from atop.

                            'Complete the weapon, slay the beast, and earn your place as a hero,'
                            are her dying words."""))
        self.player.inventory.append("shard 1")
