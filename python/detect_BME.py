#!/usr/bin/python3
import time
import board
import busio
import adafruit_bme680

# Initialisation de l'I2C
i2c = busio.I2C(board.SCL, board.SDA)

try:
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x77)  # Utilisez 0x77 si 0x76 ne fonctionne pas
    print("BME680 détecté avec succès!")
    
    # Essayer de lire des données
    temperature = bme680.temperature
    print(f"Température : {temperature:.2f} C")
except Exception as e:
    print(f"Erreur lors de l'accès au capteur : {e}")
