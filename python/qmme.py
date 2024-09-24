#!/usr/bin/python3
import time
import psutil
import board
import adafruit_bme680
import paho.mqtt.client as mqtt
from time import sleep
from busio import I2C
from gpiozero import RGBLED

my_led = RGBLED(13, 19, 26, active_high=True)# change to False for common Anode RGBLEDs RGB and Cyan Mangenta Yellow

my_led.color = (1, 0, 0)
print("Red...")
sleep(2)

my_led.color = (0, 1, 0)
print("Green...")
sleep(2)

my_led.color = (0, 0, 1)
print("Blue...")
sleep(2)

my_led.color = (1, 1, 1)
print("White...")
sleep(2)



# Initialisation de l'I2C et du capteur BME680
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x77)

# Configuration de la pression au niveau de la mer pour une mesure correcte de l'altitude
bme680.sea_level_pressure = 1016  # en hPa

# Offset de température pour ajustement
temperature_offset = -5.5

# Fonction pour convertir Celsius en Fahrenheit
def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Configuration du client MQTT
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)

# Boucle principale pour lire et publier les données du capteur et la consommation de RAM
while True:
    # Lecture des données du capteur avec compensation d'offset
    temperature_c = bme680.temperature + temperature_offset
    temperature_f = to_fahrenheit(temperature_c)
    humidity = bme680.humidity
    pressure = bme680.pressure
    altitude = bme680.altitude
    gas = bme680.gas

    # Publication des données sur des topics MQTT
    mqtt_client.publish("sensor/temperature", f"{temperature_c:.2f}")
    mqtt_client.publish("sensor/temperature_fahrenheit", f"{temperature_f:.2f}")
    mqtt_client.publish("sensor/humidity", f"{humidity:.2f}")
    mqtt_client.publish("sensor/pressure", f"{pressure:.2f}")
    mqtt_client.publish("sensor/altitude", f"{altitude:.2f}")
    mqtt_client.publish("sensor/gas", f"{gas:.2f}")

    # Affichage formaté des données dans le terminal
    print(f"Temperature: {temperature_c:.2f} °C / {temperature_f:.2f} °F")
    #print(f"VOCS (Gas Resistance): {gas} ohms")
    #print(f"Humidity: {humidity:.2f} %")
    #print(f"Pressure: {pressure:.2f} hPa")
    #print(f"Altitude: {altitude:.2f} meters")

    # Attendre 1 seconde avant la prochaine lecture
    time.sleep(1)
