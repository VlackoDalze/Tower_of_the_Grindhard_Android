import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout  # organiza los widgets de manera relativa, es decir, se ajustan automáticamente a la posición de los widgets circundantes
from kivy.lang import Builder
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

class Control(Widget):
    pass

class Map_lvl(FloatLayout):
    lvl = NumericProperty(0) #definimos la propiedad lvl se puede acceder a ella desde ambos lados self. root.
    def next_lvl(self):
        self.lvl+=1
    def saved_lvl(self, value):
        self.lvl=value
        
class TowerOfTheGrindhardApp(App):
    def build(self):
        # return BoxLayout()
        return Map_lvl()
    
    # def on_start(self): #maximizar
    #     Window.maximize()
        
        
if __name__ == '__main__':
    TowerOfTheGrindhardApp().run()
    