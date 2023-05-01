from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty


class Map_lvl(RelativeLayout):
    # definimos la propiedad lvl se puede acceder a ella desde ambos lados self. root.
    lvl = NumericProperty(0)

    def next_lvl(self):
        self.lvl += 1

    def saved_lvl(self, value):
        self.lvl = value
