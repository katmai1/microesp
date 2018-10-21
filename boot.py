# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
from pantalla import Pantalla
from wifi import Wifi

webrepl.start()
gc.collect()
wlan = Wifi()


# starting display
dis = Pantalla()

# connect to wifi
wlan.conecta("Vomistar_FB30")

dis.texto("IP: ")
dis.texto("GTW: ")
