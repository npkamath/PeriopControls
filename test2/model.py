import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Increase Temp'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='User Name')
        layout.add_widget(button)
        return layout
if __name__ == '__main__':
    MyApp().run()