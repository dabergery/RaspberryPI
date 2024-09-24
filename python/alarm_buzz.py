from gpiozero import Buzzer
from time import sleep

# Définir le buzzer connecté au GPIO 17
buzzer = Buzzer(17)

try:
    while True:
        buzzer.on()  # Allumer le buzzer
        sleep(1)     # Attendre 1 seconde
        buzzer.off() # Éteindre le buzzer
        sleep(1)     # Attendre 1 seconde
except KeyboardInterrupt:
    # Nettoyer et désactiver le buzzer en cas d'interruption
    buzzer.off()

