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
        print('network config:', self.wan.ifconfig())

    @property
    def is_connected(self):
        return self.wan.isconnected()
    
    def ifconfig(self, filtro='all'):
        datos = self.wan.ifconfig()
        if filtro == 'all':
            return datos
        elif filtro == 'ip':
            return datos[0]
        return f"el filtro '{filtro}' no es valido"

