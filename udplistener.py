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

    #Caters to the Events of Precipitation
    if (event_type == "evt_precip"):
        #Unpack json to feed into the class
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        event = json_in['evt']
        prec = udpclasses.Evt_precip(serialnum, typee, hubsn, event)
        #Convert to Json object
        jsonStr = json.dumps(prec.returnval())
        #Check with Glen
        # currentData.rain = rain;
        # rained++
        
    #Caters to the Events of Lightning Strikes
    if (event_type == "evt_strike"):
        #Unpack json to feed into the class
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        event = json_in['evt']
        strike = udpclasses.Evt_strike(serialnum,typee,hubsn,event)
        #Convert to Json object
        jsonStr = json.dumps(strike.returnval())

    #Caters to the Rapid Wind Observations
    if (event_type == "rapid_wind"):
        #Unpack json to feed into the class
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        ob = json_in['ob']
        wind = udpclasses.Rapid_wind(serialnum,typee,hubsn,ob)
        #Convert to Json object
        jsonStr = json.dumps(wind.returnval())
        
    #Caters to the Air Observations
    if (event_type == "obs_air"):
        #Unpack json to feed into the class
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        obs = json_in['obs']
        firmwarerev = json_in['firmware_revision']
        air = udpclasses.Obs_air(serialnum,typee,hubsn,obs,firmwarerev)
        #Convert to Json object
        jsonStr = json.dumps(air.returnval())
    
    #Caters to the Sky Observations
    if (event_type == "obs_sky"):
        #Unpack json to feed into the class
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        obs = json_in['obs']
        firmwarerev = json_in['firmware_revision']
        #Feed into CLass
        sky = udpclasses.Obs_sky(serialnum,typee,hubsn,obs, firmwarerev)
        #Convert to Json object
        jsonStr = json.dumps(sky.returnval())
    
    #Caters to the Device Status Event Type
    if (event_type == "device_status"):
        #Unpack json to feed into the class
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
        #Feed into CLass
        device = udpclasses.Device_status(serialnum,typee,hubsn,timestamp,uptime,voltage,
                                firmwarerev,rssi,hub_rssi,sensor_status,debug)
        #Convert to Json object
        jsonStr = json.dumps(device.returnval())

    #Caters to the Hub Status Event Type
    if (event_type == "hub_status"):
        #Unpack json to feed into the class
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
        #Feed into CLass
        hub = udpclasses.Hub_status(serialnum,typee,uptime,rssi,timestamp,resetflags,seq,fs,
                                radiostats,mqttstats)
        #Convert to Json object
        jsonStr = json.dumps(hub.returnval())

    return jsonStr
#Import Class sendtocloud as it contains method that sets up Azure
import sendtocloud

def main():
    #Instantiate Class
    toCloud = sendtocloud.QueueHelloWorldSamples()
    #Instantiate the setup Azure method
    setupqueue = toCloud.SetupAzure()
    #IP address from UDP programme for hub, always use socket as 50222
    server_address = ('192.168.88.252', 50222)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock: # No need to cleanup sockets after while loop is terminated as using with statement
        sock.settimeout(50)     #Set a timeout so that if sockets does not receive any messages for 50 seconds, it is released.
        #bind socket to IP address
        sock.bind(server_address)
        running = True      #Set Flag to true
        #Keep running loop until ctrl + C is pressed
        while running:
            try:
                data,addr = sock.recvfrom(4096) # buffer size is 1024 bytes
                #Load JSON object
                json_data = json.loads(data.decode('utf-8'))
                pushvar = sorter(json_data)     #Pushvar is a the return type of sorter method and is also a Json object
                #For debugging only
                print(pushvar)
                setupqueue.send(Message(pushvar))          #Push message to Cloud
                #toCloud.create_client_with_connection_string()
                toCloud.queue_and_messages_example(pushvar)

            #While loop is terminated if ctrl + C is pressed
            except KeyboardInterrupt:
                print("Pressing ctrl+C has terminated your the while loop")
                running = False
                sock.close()
                break

main()