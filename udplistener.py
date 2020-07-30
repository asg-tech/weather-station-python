#This file is a translation to Python of server.ts
#Wind Direction has been flipped by 180Degrees because the weatherflow tempest unit was designed in the Northern
#Hemisphere and we are using this device in the Southern Hemisphere.
import udpclasses
import json
import argparse

PATH_JSON = "C:\\Gaurang\\WeatherStation\\"

with open(PATH_JSON + 'sky.json') as json_data:
    json_data = json.load(json_data)


def sorter(json_in):
    event_type = json_in['type']
    if (event_type == "evt_precip"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        event = json_in['evt']
        udpclasses.Evt_precip(serialnum,typee, hubsn,event)
        #Check with Glen
        # currentData.rain = rain;
        # rained++
 
    if (event_type == "evt_strike"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        event = json_in['evt']
        udpclasses.Evt_strike(serialnum,typee,hubsn,event)

    if (event_type == "rapid_wind"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        ob = json_in['ob']
        udpclasses.Rapid_wind(serialnum,typee,hubsn,ob)
        # timeep, wspeed, wdirn = windclass.unpacker(ob)
        # print(windclass.printme(timeep, wspeed, wdirn))

    if (event_type == "obs_air"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        obs = json_in['obs']
        firmwarerev = json_in['firmware_revision']
        udpclasses.Obs_air(serialnum,typee,hubsn,obs,firmwarerev)
        # timeep, stationpress, airtemp, relhumid, lgtnstrike, lgtnstrikedist_avg, battery, reportint = airclass.unpacker(obs)
        # print(airclass.printme(timeep, stationpress, airtemp, relhumid, lgtnstrike, lgtnstrikedist_avg, battery, reportint))

    if (event_type == "obs_sky"):
        serialnum = json_in['serial_number']
        typee = json_in['type']
        hubsn = json_in['hub_sn']
        obs = json_in['obs']
        firmwarerev = json_in['firmware_revision']
        udpclasses.Obs_sky(serialnum,typee,hubsn,obs, firmwarerev)
        

sorter(json_data)
"""     msg_type = json_in.type

    switch(msg_type):
        case: "evt_precip":
        classpricp = new Evnt_pricip(json_in , etc)
        # inside your class unpack the array into key : value pairs ie {rain: 2}
        classpricp.printme()
        break """

""" #Pseudo Code:
test = new evt_precip(stike.serial, strike.type, strike.obs, stirke.idk)
switch herer

array = obs
volts = obs[3]
meters = obs[2]
time = obs[0]

def printme():
    print("type: {} serial {} idk {} volts: {} meters{} time {} ".format(type, serial, volrts, meters, time)) """