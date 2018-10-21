import network

class Wifi:
    redes = {
        "Vomistar_FB30": "jmz8mhafzpfxmbzt",
    }
    def __init__(self):
        self.wan = network.WLAN(network.STA_IF)

    def conecta(self, essid):
        if not self.is_connected:
            self.wan.active(True)
            self.wan.connect(essid, self.redes[essid])
            while not self.is_connected:
                pass

    @property
    def is_connected(self):
        return self.wan.isconnected()

    @property
    def ip(self):
        return self.wan.ifconfig()[0]
    
    @property
    def netmask(self):
        return self.wan.ifconfig()[1]
    
    @property
    def gateway(self):
        return self.wan.ifconfig()[2]
    
    @property
    def dns(self):
        return self.wan.ifconfig()[3]

