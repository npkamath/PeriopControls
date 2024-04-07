import kivy
kivy.require('2.1.0') # replace with your current kivy version !
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import datetime
import time


class MyApp(App):
    def build(self):
        # Create a label widget
        label = Label(text='Hello, Kivy!', font_size=50)

        # Set fullscreen mode
        self.set_fullscreen()

        return label

    def set_fullscreen(self):
        # Set fullscreen mode
        from kivy.core.window import Window
        Window.fullscreen = 'auto'

if __name__ == '__main__':
    os.environ['DISPLAY'] = ':0'
    MyApp().run()