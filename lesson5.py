#!/usr/bin/python3
import rgbLed

if __name__ == "__main__":
    rgb = rgbLed.RGBLed(22,27,17)
    rgb.redLight(second=1)
    rgb.greenLight(second=1)
    rgb.blueLight(second=1)    
    rgb.clean()
    
