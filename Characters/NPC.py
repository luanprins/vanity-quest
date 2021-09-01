from random import randint

class NPC():

    def __init__(self):
        
        self.intro_lines = ["\n\"Good day.\"",
                            "\n\"How do you do?\""
                            ]
        # Topics and their correlating question-answer pairs.
        # Keys are identical to things listed in the player's mind.
        # The content will be updated by each NPC; these are here
        # to enhance readability of following method.
        self.player_dependent_topics = {}
        self.place_dependent_topics = {}
        self.responses = {}
        self.greetings = []

    def start_dialogue(self, player, scene_name):
        # Get a random line that opens the dialogue, once per dialogue.
        print(self.intro_lines[randint(0, len(self.intro_lines) - 1)])

        while True:
            # Set dialogue_options as default scene_based topics
            dialogue_options = [topic for topic in self.place_dependent_topics[scene_name]]

            # Add topics that depend on what the player has learned.
            for topic in self.player_dependent_topics[scene_name]:
                if topic in player.mind:
                    dialogue_options.append(self.player_dependent_topics[scene_name][topic]["player line"])

            alphabetical_dialogue_options = sorted(dialogue_options)

            # Add a random greeting option from the player's repertoire.
            player_greeting = player.greetings[randint(0, len(player.greetings) - 1)]
            alphabetical_dialogue_options.append(player_greeting)

            for i in alphabetical_dialogue_options:
                print("\n" + str(alphabetical_dialogue_options.index(i) + 1) + ". " + i)

            action = input("\nEnter the number of your desired topic > ")

            # Make sure that the input can be made an integer
            # and that it is a dialogue option (if not, re-prompt.)
            try:
                int(action)
                choice = alphabetical_dialogue_options[int(action) - 1]
            except:
                print("\nNot valid input. Type a number from the list.")
                continue
            
            # If the player is leaving dialogue, return a random greeting.
            if int(action) - 1 == alphabetical_dialogue_options.index(player_greeting):
                return print(self.greetings[randint(0, len(self.greetings) - 1)])

            # Check if the player's choice is one of the default topics for the scene.
            for key in self.place_dependent_topics[scene_name]:
                if choice == key:
                    self.place_dependent_topics[scene_name][key](player)

            # See if the player's choice is one of the topics they've had to learn.
            for key in self.player_dependent_topics[scene_name]:
                if choice == self.player_dependent_topics[scene_name][key]["player line"]:
                    self.player_dependent_topics[scene_name][key]["response"](player)
