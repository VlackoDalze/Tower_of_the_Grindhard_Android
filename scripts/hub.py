from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import BooleanProperty


class Hud(FloatLayout):
    pass

class SettingButton(Button):
    def openSettings(self):
        print("asd")

class Settings(FloatLayout):
    visible = BooleanProperty(False)

    def show_layout(self):
        self.visible = True

    def hide_layout(self):
        self.visible = False

class AndroidControl(FloatLayout):
    def movePlayer(self,movement:str):
        print(movement)

class NavigationBar(FloatLayout):
    pass