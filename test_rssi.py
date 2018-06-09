from bluepy.btle import Scanner, DefaultDelegate
import paho.mqtt.publish as publish
import datetime
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self, iface=0):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
            print ("RSSI ", dev.rssi)
        elif isNewData:
            print ("Received new data from", dev.addr)

while True:
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10.0)
    for dev in devices:
        for (adtype, desc, value) in dev.getScanData():
    #        print(str(adtype) + " - " + desc + " - " + value) 
            if (desc == "Short Local Name"):
                if (value == "ADA#00011") :
                    root_topic = dev.addr + "/UTI01/RSSI" 
                    ts = time.time()
                    payload_data = (str(dev.rssi)+";"+str(ts))
                    publish.single(topic=root_topic, payload=payload_data, hostname="18.191.122.209")
                    print("Published at " + root_topic + " payload: " + payload_data)
    

