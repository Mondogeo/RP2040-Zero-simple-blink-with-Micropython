from machine import Pin
from neopixel import NeoPixel
from utime import sleep
pin = Pin(16, Pin.OUT)   # set GPI=16 to output to drive NeoPixels
np = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO16 for 1 pixel
#
''' **********************************
FUNCTION NEOPIXEL
4/4/2022 - Mauro Vannini
It can accept:
1 --> switch on the led as white
0 --> switch off the led
list/tupla of three values --> switch on the led of the indicated values (0-255) (red, green, blu)
''' 
def neo_pixel (valore):
    try:
        # se valore è una tupla/lista di 3 termini:
        if len(valore)==3:
            if 0<=valore[0]<=255 and 0<=valore[1]<=255 and 0<=valore[2]<=255:
                np[0] = valore
                np.write()
                return 1
            else:
                return 0
    except:
        try:
            if valore==0:
                np[0] = (0,0,0)
                np.write()
                return 1
            elif valore==1:
                np[0] = (255,255,255)
                np.write()
                return 1
        except:
            return 0
# ************************************
# Examples
#
neo_pixel (1) # switch on the led as white
sleep(1)
#
neo_pixel (0) # switch off the led
sleep(1)
#
neo_pixel ((150, 0, 0)) # switch on the led as red
sleep(1)
#
neo_pixel ((150, 150, 0))
sleep(1)
#
neo_pixel ((0, 150, 0)) # switch on the led as green
sleep(1)
#
neo_pixel ((0, 150, 150))
sleep(1)
#
neo_pixel ((0, 0, 150)) # switch on the lad as blu
sleep(1)
#
neo_pixel (0)


