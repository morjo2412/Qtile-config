#!/bin/bash

# Ejecuta el compositor Picom para transparencias y sombras
picom --config ~/.config/picom/picom.conf &

# Cualquier otro programa que desees ejecutar al inicio
nm-applet &  # Si usas nm-applet para gestionar Wi-Fi

feh --bg-scale /ruta/a/tu/imagen.jpg
