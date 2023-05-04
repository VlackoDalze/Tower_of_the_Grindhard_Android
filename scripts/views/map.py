from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import NumericProperty,BooleanProperty,StringProperty
from kivy.graphics.texture import TextureRegion
from kivy.graphics import Rectangle ,Canvas
      
class Map(RelativeLayout):
    # definimos la propiedad lvl se puede acceder a ella desde ambos lados self. root.
    lvl = NumericProperty(0)
    
    def next_lvl(self):
        self.lvl += 1

    def saved_lvl(self, value):
        self.lvl = value

    def setViews(self, views):
        self.clear_widgets() 
        image = Image(source='scene/level00/_composite.png').texture
        with self.canvas:
            aux=Rectangle()
            aux.texture=image

            self.add_widget(aux)
        # gl = GridLayout(cols=2, rows=2, spacing=20)
       
        # for i in range(4):
        #     gl.add_widget(Map()) 
        # self.add_widget(gl)
            
   # for view in range(views):
        #     # scatter=Scatter(size_hint=(None,None))
           
        #     img = Image(source='scene/level00/_composite.png', keep_ratio=False, allow_stretch=True)#keep_ratio pierde la relacion de aspecto y allow_stretch ocupa todo el espacio disponible
        #     # scatter.add_widget(Map())
        #     gl.add_widget(Map())
