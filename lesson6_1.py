import gpiozero as zero 
from time import sleep

if __name__ == "__main__":
    mcp3008 = zero.MCP3008(channel=7)
    while True:
        print("光敏電阻值: ",mcp3008.value)
        sleep(1)