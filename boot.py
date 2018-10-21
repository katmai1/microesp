# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
from pantalla import Pantalla
from wifi import Wifi

webrepl.start()
gc.collect()

# connect to wifi
wlan = Wifi()
wlan.conecta("Vomistar_FB30")

# starting display
dis = Pantalla()

#ip = wlan.ifconfig('ip')
#dis.texto(f"IP: {ip}")
