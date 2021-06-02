import textwrap

class PlayerCharacter():

    def __init__(self):

        self.inventory = ["heirloom ring"]
        self.mind = []
        self.power = []
        self.mind_dict = {
                "metacy butts":
                "Metacy likes to stealthily burn the behinds of passersby.",
                "metacy magic":
                "Metacy can only interact with the physical world using magic spells.",
                "metacy soulmate":
                "As soulmates, you and Metacy share a destiny spanning multiple lifetimes.",
                "metacy visible":
                "Usually humans can't see fairies, but you can see Metacy.",
                }

    def show_inventory(self):
        if len(self.inventory) == 1:
            inventory_string = self.inventory[0]
        else:
            inventory_string = ", ".join(self.inventory[:-1]) + " and " + self.inventory[-1]
        return print(textwrap.dedent(f"""
                                    Here's the crap you're carrying around:
                                    {inventory_string}"""))

    def show_mind(self):
        for i in self.mind:
            if i in self.mind_dict:
                print(self.mind_dict.get(i), "\n")

    def show_powers(self):
        power_string = ", ".join(self.power)
        return print(textwrap.dedent(f"""
                                    Here are the powers at your disposal:
                                    {power_string}"""))
