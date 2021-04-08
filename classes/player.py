#player class takes in name and gesture
class Player:

    def __init__(self, name: str, gestures: list):
        self.name = name
        self.gestures = gestures

    #return_gesture() method returns one of three gestures within the gesture list, contained within the player objects. Check to see if inputted gesture is in player object list. 
    def return_gesture(self, gesture_num):
        return self.gestures[gesture_num]


    
