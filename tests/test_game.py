import unittest
from classes.game import Game
from classes.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        gestures = ["Rock", "Paper", "Scissors"]
        self.player_1 = Player("Bob", gestures)
        self.player_2 = Player("Adam", gestures)
        self.game_state = Game(self.player_1, self.player_2)
    
    def test_game_has_player_1(self):
        self.assertEqual(self.player_1, self.game_state.player_1)
    
    def test_game_has_player_2(self):
        self.assertEqual(self.player_2, self.game_state.player_2)
    
    def test_scissors_beats_paper_player_1_wins(self):
        player_1_gesture = self.player_1.return_gesture(2)
        player_2_gesture = self.player_2.return_gesture(1)
        
        self.assertEqual("player 1 wins", self.game_state.win_state(player_1_gesture,player_2_gesture))
    
    def test_paper_beats_rock_player_1_wins(self):
        player_1_gesture = self.player_1.return_gesture(1)
        player_2_gesture = self.player_2.return_gesture(0)
        
        self.assertEqual("player 1 wins", self.game_state.win_state(player_1_gesture,player_2_gesture))
    
    def test_rock_beats_scissors_player_1_wins(self):
        player_1_gesture = self.player_1.return_gesture(0)
        player_2_gesture = self.player_2.return_gesture(2)
        
        self.assertEqual("player 1 wins", self.game_state.win_state(player_1_gesture,player_2_gesture))
    
    def test_scissors_beats_paper_player_2_wins(self):
        player_1_gesture = self.player_1.return_gesture(1)
        player_2_gesture = self.player_2.return_gesture(2)
        
        self.assertEqual("player 2 wins", self.game_state.win_state(player_1_gesture,player_2_gesture))
    
    def test_paper_beats_rock_player_2_wins(self):
        player_1_gesture = self.player_1.return_gesture(0)
        player_2_gesture = self.player_2.return_gesture(1)
        
        self.assertEqual("player 2 wins", self.game_state.win_state(player_1_gesture,player_2_gesture))
    
    def test_rock_beats_scissors_player_2_wins(self):
        player_1_gesture = self.player_1.return_gesture(2)
        player_2_gesture = self.player_2.return_gesture(0)
        
        self.assertEqual("player 2 wins", self.game_state.win_state(player_1_gesture,player_2_gesture))
    
    def test_rock_draw(self):
        player_1_gesture = self.player_1.return_gesture(0)
        player_2_gesture = self.player_2.return_gesture(0)
        
        self.assertEqual("it's a draw", self.game_state.win_state(player_1_gesture,player_2_gesture))
    
    def test_paper_draw(self):
        player_1_gesture = self.player_1.return_gesture(1)
        player_2_gesture = self.player_2.return_gesture(1)
        
        self.assertEqual("it's a draw", self.game_state.win_state(player_1_gesture,player_2_gesture))
    
    def test_scissors_draw(self):
        player_1_gesture = self.player_1.return_gesture(2)
        player_2_gesture = self.player_2.return_gesture(2)
        
        self.assertEqual("it's a draw", self.game_state.win_state(player_1_gesture,player_2_gesture))


    