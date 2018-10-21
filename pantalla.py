import machine
from ssd1306 import SSD1306_I2C

class Pantalla:
    def __init__(self, pin1=5, pin2=4):
        '''Init display'''
        i2c = machine.I2C(scl=machine.Pin(pin1), sda=machine.Pin(pin2))
        self.oled = SSD1306_I2C(128, 32, i2c)
        self.clear()
        self.texto("Pantalla iniciada")

    def clear(self, color=0):
        '''Borra el contenido de la pantalla, color puede ser 0(negro) o 1(blanco)'''
        self.oled.fill(color)
    
    def texto(self, texto):
        self.oled.text(texto, 0, 0)
        self.oled.show()
