from kivy.core.window import Window
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.lang import Builder
# organiza los widgets de manera relativa, es decir, se ajustan automáticamente a la posición de los widgets circundantes
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
import kivy
kivy.require('2.1.0')

# class Player(Widget):
#     pass


# class GameMap(Widget):
#     pass

class Root(BoxLayout):
    pass


class Control(Widget):
    pass


class TowerOfTheGrindhardApp(App):
    def build(self):
        return Root()

    # def on_start(self): #maximizar
    #     Window.maximize()


if __name__ == '__main__':
    TowerOfTheGrindhardApp().run()
