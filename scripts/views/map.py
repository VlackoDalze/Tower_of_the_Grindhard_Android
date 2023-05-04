from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import NumericProperty,BooleanProperty,StringProperty
from kivy.core.window import Window
class Floor(FloatLayout):
    def __init__(self,**kwargs):
        super(Floor, self).__init__(**kwargs)
        size_texture=100
        limit_texture=Window.size[0]
        num_rects=int(limit_texture/size_texture)
        'assets/misc/unseen_item_old.png'
        for i in range(num_rects):
            with self.canvas:
                Rectangle(pos=(i*size_texture, 1), size=(size_texture, size_texture),source='assets/dungeon/floor/cobble_blood_8_new.png')
      
class Sky(FloatLayout):
    pass
class Background(FloatLayout):
    pass
         
class Map(RelativeLayout):
    # definimos la propiedad lvl se puede acceder a ella desde ambos lados self. root.
    lvl = NumericProperty(0)
    
    def next_lvl(self):
        self.lvl += 1

    def saved_lvl(self, value):
        self.lvl = value

    def setViews(self, views):
        self.clear_widgets()
        
        # gl = GridLayout(cols=2, rows=2, spacing=20)
        
        for view in range(views):
            # # img = Image(source='scene/level00/_composite.png', keep_ratio=False, allow_stretch=True)#keep_ratio pierde la relacion de aspecto y allow_stretch ocupa todo el espacio disponible
           self.add_widget(Floor())
       

