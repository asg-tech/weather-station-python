#This file is a translation to Python of server.ts
#Wind Direction has been flipped by 180Degrees because the weatherflow tempest unit was designed in the Northern
#Hemisphere and we are using this device in the Southern Hemisphere.
import udpclasses
import json
import argparse
import socket
from azure.servicebus import Message
# PATH_JSON = "C:\\Gaurang\\WeatherStation\\"

# with open(PATH_JSON + 'air.json') as json_data:
#     json_data = json.load(json_data)

def sorter(json_in):
    event_type = json_in['type']

    #print("type received {}".format(event_type))

    if (event_type == "evt_precip"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        event = json_in['evt']
        prec = udpclasses.Evt_precip(serialnum, typee, hubsn, event)
        jsonStr = json.dumps(prec).__dict__
        print(jsonStr)
        #Check with Glen
        # currentData.rain = rain;
        # rained++
        
 
    if (event_type == "evt_strike"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        event = json_in['evt']
        jsonStr = json.dumps(udpclasses.Evt_strike(serialnum,typee,hubsn,event).__dict__)

    if (event_type == "rapid_wind"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        ob = json_in['ob']
        jsonStr = json.dumps(udpclasses.Rapid_wind(serialnum,typee,hubsn,ob).__dict__)
        
    if (event_type == "obs_air"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        obs = json_in['obs']
        firmwarerev = json_in['firmware_revision']
        jsonStr = json.dumps(udpclasses.Obs_air(serialnum,typee,hubsn,obs,firmwarerev).__dict__)
        
    if (event_type == "obs_sky"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        obs = json_in['obs']
        firmwarerev = json_in['firmware_revision']
        jsonStr = json.dumps(udpclasses.Obs_sky(serialnum,typee,hubsn,obs, firmwarerev).__dict__)
    
    if (event_type == "device_status"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        timestamp = json_in['timestamp']
        uptime = json_in['uptime']
        voltage = json_in['voltage']
        firmwarerev = json_in['firmware_revision']
        rssi = json_in['rssi']
        hub_rssi = json_in['hub_rssi']
        sensor_status = json_in['sensor_status']
        debug = json_in['debug']
        jsonStr = json.dumps(udpclasses.Device_status(serialnum,typee,hubsn,timestamp,uptime,voltage,
                                firmwarerev,rssi,hub_rssi,sensor_status,debug).__dict__)


    if (event_type == "hub_status"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        uptime = json_in['uptime']
        rssi = json_in['rssi']
        timestamp = json_in['timestamp']
        resetflags = json_in['reset_flags']
        seq = json_in['seq']
        fs = json_in['fs']
        radiostats = json_in['radio_stats']
        mqttstats = json_in['mqtt_stats']
        jsonStr = json.dumps(udpclasses.Hub_status(serialnum,typee,uptime,rssi,timestamp,resetflags,seq,fs,
                                radiostats,mqttstats).__dict__)
    
    return jsonStr    

import sendtocloud
#from sendtocloud import *
def main():

    toCloud = sendtocloud.QueueHelloWorldSamples()
    setupqueue = toCloud.SetupAzure()
    server_address = ('192.168.88.252', 50222)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock: # UDP
        sock.settimeout(50)
        sock.bind(server_address)
        #sock.listen()
        #s.setblocking(0)
        running = True
        while running:
            try:
                data,addr = sock.recvfrom(4096) # buffer size is 1024 bytes
                #print("received message: %s" % data)
                json_data = json.loads(data.decode('utf-8'))
                pushvar = sorter(json_data)
                print(pushvar)
                setupqueue.send(Message(pushvar))
                #toCloud.create_client_with_connection_string()
                toCloud.queue_and_messages_example(pushvar)

            except KeyboardInterrupt:
                print("Pressing ctrl+C has terminated your the while loop")
                running = False
                sock.close()
                break

main()