from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import NumericProperty,BooleanProperty
from kivy.utils import platform
from scripts.hub import Hud
        
class Map_lvl(RelativeLayout):
    # definimos la propiedad lvl se puede acceder a ella desde ambos lados self. root.
    lvl = NumericProperty(0)

   
    def addButtoms(self):
        if platform == 'win':
            self.add_widget(Hud())
    
    def next_lvl(self):
        self.lvl += 1

    def saved_lvl(self, value):
        self.lvl = value

