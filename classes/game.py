from classes.player import Player
class Game:

    #init function takes, 2 player objects as arguments
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2

    #win_state() function takes in 2 gesture strings and returns a formatted string declaring the winner
    def win_state(self, player_1_gesture, player_2_gesture):
        if player_1_gesture == player_2_gesture:
            return "it's a draw"
        elif player_1_gesture == "Scissors":
            if player_2_gesture == "Paper":
                return "player 1 wins"
            elif player_2_gesture == "Rock":
                return "player 2 wins"
        elif player_1_gesture == "Rock":
            if player_2_gesture == "Scissors":
                return "player 1 wins"
            elif player_2_gesture == "Paper":
                return "player 2 wins"
        elif player_1_gesture == "Paper":
            if player_2_gesture == "Rock":
                return "player 1 wins"
            elif player_2_gesture == "Scissors":
                return "player 2 wins"
        
        



    