import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

# class Player(Widget):
#     pass


# class GameMap(Widget):
#     pass

class Control(Widget):
    pass

class TowerOfTheGrindhardApp(App):
    def build(self):
        return BoxLayout()

if __name__ == '__main__':
    TowerOfTheGrindhardApp().run()