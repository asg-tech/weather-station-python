#This file is a translation to Python of server.ts
#Wind Direction has been flipped by 180Degrees because the weatherflow tempest unit was designed in the Northern
#Hemisphere and we are using this device in the Southern Hemisphere.
import udpclasses
import json
import argparse
import socket
import sys
import time
from sendtocloud import sendWeatherData, sendWindBeringData
# PATH_JSON = "C:\\Gaurang\\WeatherStation\\"

allowedMessageTypes = ["evt_precip", "evt_strike", "rapid_wind",
 "obs_air", "obs_sky", "device_status", "hub_status"];

# list of dict for wind ave data
listOfPackets = []

start_time = time.time()

# add data to list as dict
# correct wind direction for Southern Hemisphere
# the solar pannel requires the instalation to be 180 degrees out from north marker
def processWindDataAve(widdir, wdspd, tim):
    # if wind direction is greater than 180
    if widdir > 180:
        # remove 180 from wind dir
        widdir = widdir - 180
    # if wind direction is less than 180 
    elif widdir < 180:
        # add 180 to wind dir
        widdir = widdir + 180
    # if the wind is at 0/360
    elif widdir == 0 or widdir == 360:
        # set the dir to 180
        widdir == 180
    # if wind dir is 180
    elif widdir == 180:
        # set to 0/360
        widdir == 0
    packet = { "bering": widdir, "speed": wdspd, "time": tim }
    listOfPackets.append(packet)

# calculate average and post to topic
def calculateAvg():
    global start_time
    if(start_time + 240 < time.time()):
        global listOfPackets
        under = []
        count = 0
        total_bearing = 0
        total_speed = 0

        for entry in listOfPackets:
            # if the time stored is less than last run pus 10 mins
            if(entry["time"] < (start_time + 600)):
                count += 1
                total_speed += entry["speed"]
                total_bearing += entry["bering"]
                under.append(entry)
            else:
                print("older than "+ (start_time + 600))
        # remove all packets over 10 mins
        listOfPackets = under
        # reset start time
        start_time = time.time()
        # calculate average
        if(total_bearing != 0 and total_speed != 0):
            average = total_bearing / count
            speed_avg = total_speed / count
            print("AVERAGE BEARING: {} speed: {}".format(average, speed_avg))
            ave = { 
                "bering_average": average,
                "speed_average": speed_avg,
                "time": start_time 
            }
            pacAve = json.dumps(ave)
            sendWindBeringData(pacAve)
            print("SENDING AVG")

def sorter(json_in):
    event_type = json_in['type']
    jsonStr = {"type":"none"}

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

        tim = ob[0]
        wdspd = ob[1]
        widdir = ob[2]
        processWindDataAve(widdir, wdspd, tim)


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
        firmwarerev = json_in['firmware_revision']
        uptime = json_in['uptime']
        rssi = json_in['rssi']
        timestamp = json_in['timestamp']
        resetflags = json_in['reset_flags']
        seq = json_in['seq']
        fs = json_in['fs']
        radiostats = json_in['radio_stats']
        mqttstats = json_in['mqtt_stats']
        #Feed into CLass
        hub = udpclasses.Hub_status(serialnum,typee, firmwarerev,uptime,rssi,timestamp,resetflags,seq,fs,
                                radiostats,mqttstats)
        #Convert to Json object
        jsonStr = json.dumps(hub.returnval())

    return jsonStr
#Import Class sendtocloud as it contains method that sets up Azure
import sendtocloud

def startloop():
    #Instantiate Class
    #toCloud = sendtocloud.QueueHelloWorldSamples()
    #Instantiate the setup Azure method
    #setupqueue = toCloud.SetupAzure()
    #IP address from UDP programme for hub, always use socket as 50222
    server_address = ('0.0.0.0', 50222)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock: # No need to cleanup sockets after while loop is terminated as using with statement
        sock.settimeout(120)     #Set a timeout so that if sockets does not receive any messages for 50 seconds, it is released.
        #bind socket to IP address
        sock.bind(server_address)
        running = True      #Set Flag to true
        #Keep running loop until ctrl + C is pressed
        while running:
            try:
                data,addr = sock.recvfrom(4096) # buffer size is 1024 bytes
                #Load JSON object
                if(data):
                    json_data = json.loads(data.decode('utf-8'))
                    pushvar = sorter(json_data)     #Pushvar is a the return type of sorter method and is also a Json object
                    #For debugging only

                    #obs = json_data["type"]
                    #print("obs decoded {}".format(obs))
                    if json_data['type'] in allowedMessageTypes:
                        sendWeatherData(pushvar)
                        print(pushvar)
                time_now = time.time()

                calculateAvg()
            #socket timeout exception here
            except socket.timeout:
                print("Socket timeout 120 seconds with no messages")
                running = False
                sock.close()
                break

            #While loop is terminated if ctrl + C is pressed
            except KeyboardInterrupt:
                print("Pressing ctrl+C has terminated your the while loop")
                running = False
                sock.close()
                break

print("UDPlistener starting -> ")
startloop()
print("->  Closing")