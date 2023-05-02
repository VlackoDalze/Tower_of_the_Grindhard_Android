from kivy.core.window import Window
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.lang import Builder

# organiza los widgets de manera relativa, es decir, se ajustan automáticamente a la posición de los widgets circundantes
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App

# hacer esto para importar clases y que no pete al darle a run()
from scripts.map import Map_lvl
from scripts.control import Control
from scripts.menus import MenuCreateCharacter,MenuSelectCharacter,MenuSelectNumPlayers,MenuStart
from scripts.login import Login
from scripts.root import Root
from scripts.sounds import SoundsMaster
from scripts.button_settings import  ButtonSettingsContainer

import kivy

kivy.require("2.1.0")

print(kivy.__version__)
class TowerOfTheGrindhardApp(App):
    def build(self):
        self.playMusicLoop()
        return Root()

    def playMusicLoop(self, *args):
        SoundsMaster.playMusic()
        Clock.schedule_once(self.playMusicLoop, 2)  # Ejecuta el método cada 1 segundos

    def my_callback(self, instance):
        print("El botón ha sido presionado")


if __name__ == "__main__":
    TowerOfTheGrindhardApp().run()
