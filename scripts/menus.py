from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class MenuSelectCharacter(RelativeLayout):

   pass
       
class MenuStart(RelativeLayout):
    def verifyPlatform(self):
        if platform=='win':
            return 'menu_selectNumPlayers' 
        elif platform=='android':
            return 'login'       
        
class MenuSelectNumPlayers(RelativeLayout):
   
    
    number_players = NumericProperty(0)
    def defineNumberOfPlayers(self,num): 
        MenuSelectNumPlayers.number_players= num
        print( MenuSelectNumPlayers.number_players)
        return 'login'
    
    
class MenuCreateCharacter(RelativeLayout):
    pass
