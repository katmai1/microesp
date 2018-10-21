import network

class Wifi:
    redes = {
        "Vomistar_FB30": "jmz8mhafzpfxmbzt",
    }
    def __init__(self):
        self.wan = network.WLAN(network.STA_IF)

    def conecta(self, essid):
        if not self.is_connected():
            self.wan.active(True)
            self.wan.connect(essid, self.redes[essid])
            while not self.is_connected():
                pass

    @property
    def is_connected(self):
        return self.wan.isconnected()

    @property
    def ip(self):
        return self.wan.ifconfig()[0]

