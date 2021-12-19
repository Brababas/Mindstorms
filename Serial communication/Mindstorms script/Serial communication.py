import utime
import hub

vcp = hub.USB_VCP(0)

firstTime = 0

while True:
    if vcp.isconnected():
        hub.display.show(hub.Image.HAPPY)
        if firstTime == 0:
            vcp.write("narf\n")
            firstTime += 1
        utime.sleep(10)
    else:
        hub.display.show(hub.Image.SAD)
    utime.sleep(1)