from Universe.Scene import Scene
import textwrap

class Scene4_CrystalRoom(Scene):

    def enter(self):
        print(textwrap.dedent("""
                            You stand in a room made out of crystals.

                            Inside the crystals, scenes from countless
                            lives are playing out. People are being mutilated
                            by giant bears in some, and getting married in
                            others.



                            """))
