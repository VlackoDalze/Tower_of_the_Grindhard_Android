from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager

aux_BBDD=[{'admin': '1234'},{'user01': 'gamba'}]

class Login(RelativeLayout):
    
    intents_number=0
 
    def validate_inputs(self):

        if Login.intents_number<3:
            username = self.ids.username_input.text
            password = self.ids.password_input.text

            for user in aux_BBDD:
                if username in user.keys() and password == user[username]:
                    return True
                else:
                    Login.intents_number+=1
                    popup = Popup(title='Error de autenticación', 
                                content=Label(text='El usuario o la contraseña son incorrectos\nnumero de intentos '+str(Login.intents_number)),
                                size_hint=(None, None), size=(400, 200))
                    popup.open()
                    
                    return False

        else:
            popup = Popup(title='Usuario Bloqueado', 
                                content=Label(text='Cuenta bloqueada, reinica la aplicacion \no comuniquese con soporte'),
                                size_hint=(None, None), size=(400, 200))
            popup.open()
            

  