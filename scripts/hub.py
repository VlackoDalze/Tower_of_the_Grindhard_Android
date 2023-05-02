from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty,BooleanProperty,StringProperty
from kivy.utils import platform
    

class Hud(FloatLayout):
    pass

class ScreenReceiver():
    screenName = ''

    @staticmethod
    def saveScreenName(screenName:str):
        SettingButton.screenName = screenName

    @staticmethod
    def getScreenName() -> str:
        return SettingButton.screenName

class SettingButton(Button):

    def saveScreenName(self,screenName:str):
        print("saving screen name")
        ScreenReceiver.saveScreenName(screenName) 

class CloseSettingButton(Button):
    def getScreenName(self):
        print("Getting screen name")
        return ScreenReceiver.getScreenName()

class Settings(FloatLayout):
    pass

class AndroidControl(FloatLayout):
    
    prop_plataform=StringProperty(platform)
    
    def movePlayer(self,movement:str):
        print(movement)
    

class NavigationBar(FloatLayout):
    pass