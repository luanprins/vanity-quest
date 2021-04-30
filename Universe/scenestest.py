class ParentScene:

    def __init__(self):
        pass

    def enter(self):

        self.action = input("\n> ")

        if self.action == "help":
            print("This is the help output.")
            return
        elif self.action == "inventory":
            print("This is the inventory output.")
            return
        elif self.action == "think":
            print("This is the think output.")
            return
        else:
            print("Not a valid input.")
            return

class ChildScene(ParentScene):

    def __init__(self):
        super().__init__()

    def enter(self):
        while True:
            super().enter()
            if self.action == "test":
                print("This is the test output.")
                continue
            elif self.action == "win":
                print("This is the win output.")
                return print("You win!")

scene_go = ChildScene()

scene_go.enter()