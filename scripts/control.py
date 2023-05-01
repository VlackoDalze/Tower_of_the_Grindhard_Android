from kivy.uix.floatlayout import FloatLayout
import enum

class Movement(enum.Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4


class Control(FloatLayout):
    def movePlayer(self, movement:Movement):
        print(movement)