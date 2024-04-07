import kivy
kivy.require('2.1.0')  # replace with your current kivy version!
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Mattress Temperature Section
        self.mattress_temp = 30.0  # Initial mattress temperature
        mattress_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='48dp')
        mattress_label = Label(text='Mattress Temperature: ')
        self.mattress_temp_label = Label(text=f'{self.mattress_temp}°C')
        mattress_layout.add_widget(mattress_label)
        mattress_layout.add_widget(self.mattress_temp_label)
        
        layout.add_widget(mattress_layout)

        # Button Section
        # Creating a new layout for buttons to be in the center-ish of the screen
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), width='200dp', height='100dp', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        up_button = Button(text='↑', size_hint=(None, None), size=('100dp', '100dp'))
        up_button.bind(on_press=self.increase_mattress_temp)
        down_button = Button(text='↓', size_hint=(None, None), size=('100dp', '100dp'))
        down_button.bind(on_press=self.decrease_mattress_temp)
        buttons_layout.add_widget(up_button)
        buttons_layout.add_widget(down_button)
        
        # Placing the buttons layout in the center of the main layout
        layout.add_widget(buttons_layout)

        # Human Temperature Section
        human_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='48dp')
        human_label = Label(text='Human Temperature: ')
        human_temp_label = Label(text='30°C')  # Placeholder for human temperature
        human_layout.add_widget(human_label)
        human_layout.add_widget(human_temp_label)

        layout.add_widget(human_layout)

        return layout

    def increase_mattress_temp(self, instance):
        self.mattress_temp += 0.5
        self.mattress_temp_label.text = f'{self.mattress_temp}°C'

    def decrease_mattress_temp(self, instance):
        self.mattress_temp -= 0.5
        self.mattress_temp_label.text = f'{self.mattress_temp}°C'

if __name__ == '__main__':
    os.environ['DISPLAY'] = ':0'
    MyApp().run()
