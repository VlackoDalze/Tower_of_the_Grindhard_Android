from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from scripts.views.menus import MenuCreateCharacter, MenuSelectCharacter, MenuSelectNumPlayers, MenuStart
from scripts.tools.hub import Hud,Settings,InventoryScreen
from scripts.views.login import Login
from scripts.views.map import Map
from scripts.tools.settings_buttons_container import SettingsButtonContainer
class Root(ScreenManager):
    num_players=NumericProperty(0)
    def __init__(self,**kwargs):
        super(Root, self).__init__(**kwargs)
        self.bind(num_players=self.set_viewsToMap)
        self.size_hint=(1,1)
        
    def createScreen(new_name:str, elements:list):
        screen= Screen( name=new_name)
        for element in elements:
            screen.add_widget(element)
        return screen
    
    def addAllScreens(self):
        self.add_widget(Root.createScreen( 'screen_start',[MenuStart()]))
        self.add_widget(Root.createScreen( 'screen_selectNumPlayers',[MenuSelectNumPlayers(),SettingsButtonContainer()]))
        self.add_widget(Root.createScreen( 'screen_login',[Login(),SettingsButtonContainer()]))
        self.add_widget(Root.createScreen( 'screen_selectCharacter',[MenuSelectCharacter(),SettingsButtonContainer()]))
        self.add_widget(Root.createScreen( 'screen_createCharacter',[MenuCreateCharacter(),SettingsButtonContainer()]))
        self.add_widget(Root.createScreen( 'screen_map',[Map(),Hud()]))
        self.add_widget(Root.createScreen( 'screen_settings',[Settings()]))
        self.add_widget(Root.createScreen( 'screen_inventory',[InventoryScreen()]))
 
    def find_screen_by_name(self, screen_name):
        for screen in self.screens:
            if screen.name == screen_name:
                return screen
        return None  
    
    def set_viewsToMap(self, instance,*args):   #s5 c1 c0 c0 text
        #self.screens[5].children[1].children[0].children[0].text=str(self.num_players)
        self.screens[5].children[1].setViews(self.num_players)