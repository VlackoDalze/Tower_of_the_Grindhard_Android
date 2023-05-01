import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder

# class Player(Widget):
#     pass


# class GameMap(Widget):
#     pass

class RootWidget(BoxLayout):
    pass

class CustomLayout(FloatLayout):
    pass

class Control(Widget):
    pass

class TowerOfTheGrindhardApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    TowerOfTheGrindhardApp().run()