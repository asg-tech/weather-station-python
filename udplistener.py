#This file is a translation to Python of server.ts
#Wind Direction has been flipped by 180Degrees because the weatherflow tempest unit was designed in the Northern
#Hemisphere and we are using this device in the Southern Hemisphere.
import udpclasses
import json
import argparse

PATH_JSON = "C:\\Gaurang\\WeatherStation\\"

with open(PATH_JSON + 'air.json') as json_data:
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
        udpclasses.Device_status(serialnum,typee,hubsn,timestamp,uptime,voltage,
                                firmwarerev,rssi,hub_rssi,sensor_status,debug)

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
        udpclasses.Hub_status(serialnum,typee,uptime,rssi,timestamp,resetflags,seq,fs,
                                radiostats,mqttstats)

sorter(json_data)