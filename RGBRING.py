
import time
import board
import neopixel
pixel_pin = board.D18  #GPIO PIN
num_pixels = 12  #how many LEDs
ORDER = neopixel.GRB  

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

pixels.fill((255, 255, 255))
pixels.show()
