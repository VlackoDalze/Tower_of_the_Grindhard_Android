from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class MenuSelectCharacter(RelativeLayout):

   pass
       
class MenuStart(RelativeLayout):
    def verifyPlatform(self):
        if platform=='win':
            return 'screen_selectNumPlayers' 
        elif platform=='android':
            return 'screen_login'       
        
class MenuSelectNumPlayers(RelativeLayout):
    def defineNumberOfPlayers(self,num):     
        self.parent.parent.num_players=num
        print(  self.parent.parent.num_players)
        return 'screen_login'
    
    
class MenuCreateCharacter(RelativeLayout):
    pass
