import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import datetime


class MyApp(App):
    def update_time(self, *args):
        self.label.text = datetime.now().strftime('%H:%M:%S')

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text=datetime.now().strftime('%H:%M:%S'))
        layout.add_widget(self.label)
        Clock.schedule_interval(self.update_time, 1)  # Update every second
        return layout
if __name__ == '__main__':
    MyApp().run()