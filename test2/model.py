import kivy
kivy.require('2.1.0')  # replace with your current kivy version!
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import smbus2
import time

class SHT30:
    def __init__(self, bus_number=1):
        self.bus = smbus2.SMBus(bus_number)
        self.address = 0x44  # SHT30 I2C address

    def read_temperature_humidity(self):
        # Send measurement command, 0x2C(44), 0x06(06) High repeatability measurement
        self.bus.write_i2c_block_data(self.address, 0x2C, [0x06])
        time.sleep(0.5)  # Wait for the measurement to complete

        # Read 6 bytes of data: temperature and humidity
        data = self.bus.read_i2c_block_data(self.address, 0x00, 6)

        # Convert the data
        cTemp = ((((data[0] * 256.0) + data[1]) * 175) / 65535.0) - 45
        humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

        return cTemp, humidity

class MyApp(App):
    def build(self):
        self.sensor = SHT30()

        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Sensor Temperature and Humidity Section
        self.sensor_temp_label = Label(text='Sensor Temperature: -- °C')
        self.sensor_humidity_label = Label(text='Sensor Humidity: -- %RH')
        layout.add_widget(self.sensor_temp_label)
        layout.add_widget(self.sensor_humidity_label)

        # Update the sensor readings every 2 seconds
        Clock.schedule_interval(self.update_sensor_readings, 2)

        return layout

    def update_sensor_readings(self, dt):
        cTemp, humidity = self.sensor.read_temperature_humidity()
        self.sensor_temp_label.text = f'Sensor Temperature: {cTemp:.2f} °C'
        self.sensor_humidity_label.text = f'Sensor Humidity: {humidity:.2f} %RH'

if __name__ == '__main__':
    os.environ['DISPLAY'] = ':0'
    MyApp().run()
