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
from smbus2 import SMBus
import time


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.cols = 3
        self.time_label = Label(text="Time: ")
        # Adding time label to top right corner
        layout.add_widget(self.time_label)
        layout.add_widget(Label())  # Spacer to push the time label to the right
        self.temp_label = Label(text="Temperature: ")
        self.humidity_label = Label(text="Humidity: ") 
        layout.add_widget(self.temp_label)
        layout.add_widget(self.humidity_label)
        
       

        Clock.schedule_interval(self.update_time, 1) 
        return layout
    def update_time(self, dt):
        self.time_label.text = "Time: " + datetime.now().strftime('%H:%M:%S')
        def on_start(self):
            # Get I2C bus
            bus = SMBus(1)

            while True:
                # SHT30 address, 0x44(68)
                # Send measurement command, 0x2C(44)
                #       0x06(06)    High repeatability measurement
                bus.write_i2c_block_data(0x44, 0x2C, [0x06])

                time.sleep(0.5)

                # SHT30 address, 0x44(68)
                # Read data back from 0x00(00), 6 bytes
                # cTemp MSB, cTemp LSB, cTemp CRC, Humididty MSB, Humidity LSB, Humidity CRC
                data = bus.read_i2c_block_data(0x44, 0x00, 6)

                # Convert the data
                cTemp = ((((data[0] * 256.0) + data[1]) * 175) / 65535.0) - 45
                fTemp = cTemp * 1.8 + 32
                humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

                # Update labels
                self.temp_label.text = "Temperature: {:.2f}°C / {:.2f}°F".format(cTemp, fTemp)
                self.humidity_label.text = "Humidity: {:.2f}%".format(humidity)

                time.sleep(2)  # Update every 2 seconds 

if __name__ == '__main__':
    MyApp().run()