import machine
from time import sleep
from ssd1306 import SSD1306_I2C

class Pantalla:
    def __init__(self, pin1=5, pin2=4):
        '''Init display'''
        i2c = machine.I2C(scl=machine.Pin(pin1), sda=machine.Pin(pin2))
        self.oled = SSD1306_I2C(128, 32, i2c)
        self.clear()

    def clear(self, color=0):
        '''Borra el contenido de la pantalla, color puede ser 0(negro) o 1(blanco)'''
        self.oled.fill(color)
        self.pos = 0
    
    def texto(self, texto):
        inicio = 0
        self.oled.text(texto, inicio, self.pos)
        self.oled.show()
        self.pos += 10
