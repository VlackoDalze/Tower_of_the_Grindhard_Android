from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import NumericProperty,BooleanProperty,StringProperty

        
class Map(RelativeLayout):
    # definimos la propiedad lvl se puede acceder a ella desde ambos lados self. root.
    lvl = NumericProperty(0)
    
    def next_lvl(self):
        self.lvl += 1

    def saved_lvl(self, value):
        self.lvl = value

    

