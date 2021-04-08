import unittest
from classes.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        
        self.gestures = ["Rock", "Paper", "Scissors"]
        self.player_1 = Player("Bob", self.gestures)
        
    def test_player_has_name(self):
        self.assertEqual("Bob", self.player_1.name)

    def test_player_has_gestures(self):
        self.assertEqual(3, len(self.player_1.gestures))
    
    def test_player_gesture_return_paper(self):
        self.assertEqual(self.gestures[1], self.player_1.return_gesture(1))
    
    def test_player_gesture_return_rock(self):
        self.assertEqual(self.gestures[0], self.player_1.return_gesture(0))

    def test_player_gesture_return_scissors(self):
        self.assertEqual(self.gestures[2], self.player_1.return_gesture(2))