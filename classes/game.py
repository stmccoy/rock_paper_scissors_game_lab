from classes.player import Player
class Game:

    #init function takes, 2 player objects as arguments
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2

    #win_state() function takes in 2 gesture strings and returns a formatted string declaring the winner
    def win_state(self, player_1_gesture, player_2_gesture):
        if player_1_gesture == "Scissors" and player_2_gesture == "Paper":
            return "player 1 wins"

    # needs if statements for every outcome but we ran out of time    

    