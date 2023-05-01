from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager


class Root(BoxLayout):
    screen_manager = ObjectProperty(None)
    menu_screen = ObjectProperty(None)
    map_screen = ObjectProperty(None)
    menu_isOk = False

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        value = 'menu'
        # crear las pantallas de menú y mapa
        menu_screen = Screen(name='menu')
        map_screen = Screen(name='mapa')

        # obtener una referencia al screen_manager
        screen_manager = self.ids.screen_manager

        # agregar las pantallas al screen_manager
        screen_manager.add_widget(menu_screen)
        screen_manager.add_widget(map_screen)

        # establecer la pantalla actual en el menú
        screen_manager.transition.direction = 'left'
        if Root.menu_isOk:
            value = 'mapa'

        screen_manager.current = value
