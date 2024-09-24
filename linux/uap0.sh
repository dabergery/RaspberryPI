#!/bin/bash

sudo iw dev wlan0 interface add uap0 type __ap
sleep 1
sudo ifconfig uap0 10.3.141.1 netmask 255.255.255.0 up
ip a | grep inet
echo "uap0 interface created and configured successfully."
echo "Demarrage du point d'acces Wifi en cours..."
sudo systemctl restart dnsmasq
sudo systemctl restart hostapd
sudo systemctl status hostapd
