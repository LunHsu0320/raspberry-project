import gpiozero as zero 
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import requests

if __name__ == "__main__":
    mcp3008_ch7 = zero.MCP3008(channel=7)
    mcp3008_ch6 = zero.MCP3008(channel=6)
    try:
        while True:
            value =round(mcp3008_ch7.value*100)
            print("光敏電阻值: ",value)
            if value>20:
                print("光線亮")
            else:
                print("光線暗")    
                
            datetimeStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            
            print("LM35",mcp3008_ch6.value*100*3.3)    
            
            response = requests.get("https://lunhsu0320-urban-space-guide-rj4w79rpjgjf479-8000.preview.app.github.dev/raspberry?time={datetimeStr}&light={value}&temprature={mcp3008_ch6.value}")
            
            if response.ok:
                print("update")
                print(response.text)
            else:
                print(response.status_code)
            
            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("程式停止")            