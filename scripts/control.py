from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class Control(FloatLayout):
    pass


class SettingButton(Button):
    def movePlayer(self, movement):
        print(movement)
