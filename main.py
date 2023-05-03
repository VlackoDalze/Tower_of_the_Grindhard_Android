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
from scripts.views.map import Map
from scripts.tools.hub import Hud
from scripts.views.menus import MenuCreateCharacter, MenuSelectCharacter, MenuSelectNumPlayers, MenuStart
from scripts.views.login import Login
from scripts.root import Root
from scripts.tools.sounds import SoundsMaster
from scripts.tools.settings_buttons_container import SettingsButtonContainer

import kivy

kivy.require("2.1.0")
print(kivy.__version__)

class StartGame():
    def start():
        start=Root()
        start.addAllScreens()
        return start
    

class TowerOfTheGrindhardApp(App):
    def build(self):
        #Window.borderless = True  # eliminar el marco de la ventana
        #Window.fullscreen = True  # todor el marco de la ventana
        Window.maximize()  # maximizar la ventana
        self.playMusicLoop()
        self.main=StartGame.start()
        return self.main

    def playMusicLoop(self, *args):
        SoundsMaster.playMusic()
        # Ejecuta el método cada 1 segundos
        Clock.schedule_once(self.playMusicLoop, 2)

    def my_callback(self, instance):
        print("El botón ha sido presionado")


if __name__ == "__main__":
    TowerOfTheGrindhardApp().run()
