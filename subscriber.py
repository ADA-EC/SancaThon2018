import paho.mqtt.client as paho
import django
import os
import sys
import datetime
import django.utils.timezone as timezone

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path + '/microcare')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microcare.settings')
django.setup()
from interface.models import Device, Movement


def on_message(mosq, obj, msg):
    print ("%-20s %d %s" % (msg.topic, msg.qos, msg.payload))
#    mosq.publish('pong', 'ack', 0)
    
    try:
        (mac_addr, position, rssi) = msg.topic.split("/")
    except ValueError:
        print("Topic must be format: mac_address/board_id/rssi")
    data = str(msg.payload).replace("'", "")
    data = data.replace("b-", "")
    (rssi_value, time_stamp) = data.split(";")
    time_stamp = datetime.datetime.fromtimestamp(int(float(time_stamp)), tz=timezone.utc)
    device = Device.objects.get(mac_address=mac_addr)
    #device = Device(mac_address=mac_addr)
    #device.save()
    
    print(time_stamp)
    print(device.last_seen)
    diff_dt = time_stamp - device.last_seen
    diff = diff_dt.total_seconds()
    device_power = device.power

    if diff > 10:
        device_power = device_power + (diff-10)			
    if int(rssi_value) < device_power:
        if device.last_position != position:
            if device.num_moves == 3:
                movement = Movement(device=device, old_position=device.last_position, new_position=position, when=time_stamp)
                movement.save()
                device.num_moves = 0
                device.power = int(rssi_value)
                device.last_position = position
                device.last_seen = time_stamp 
            else:
                device.num_moves += 1
        else:
            device.num_moves = 0
            device.power = int(rssi_value)
            device.last_position = position
            device.last_seen = time_stamp 
        print(device.num_moves)            
        device.save()		

def on_publish(mosq, obj, mid):
    pass

if __name__ == '__main__':
    client = paho.Client()
    client.on_message = on_message
    client.on_publish = on_publish

    #client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    client.connect("127.0.0.1", 1883, 60)

    client.subscribe("#", 0)

    while client.loop() == 0:
        pass

# vi: set fileencoding=utf-8 :
