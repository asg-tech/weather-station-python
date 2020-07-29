import numpy as np
import pandas as pd

#This file is a translation to Python of enum.ts

class Evt_precip:

    def __init__(self,serial_number,typee,hub_sn,evt):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.evt = evt

    def unpacker(self,evt):
        timeep = evt[0]
        return timeep

    def printme(self,time_epoch):
        return "THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {}".format(self.serial_number, self.typee, self.hub_sn, time_epoch)

class Evt_strike:

    def __init__(self,serial_number,typee,hub_sn,evt):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.evt = evt

    def unpacker(self,evt):
        timeep = evt[0]
        Distance = evt[1]
        Energy = evt[2]
        return timeep, Distance, Energy

    def printme(self,time_epoch, Distance, Energy):
        return "THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, Distance: {} meters, Energy: {}".format(self.serial_number, self.typee, self.hub_sn, time_epoch, Distance, Energy)

class Rapid_wind:

    def __init__(self,serial_number,typee,hub_sn,ob):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.ob = ob

    def unpacker(self,ob):
        timeep = ob[0]
        windspeed = ob[1]
        winddirn = ob[2]
        return timeep, windspeed, winddirn

    def printme(self,time_epoch, windspeed, winddirn):
        return "THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, WindSpeed: {} m/sec, WindDirection: {} Degrees".format(self.serial_number, self.typee, self.hub_sn, time_epoch, windspeed, winddirn)

class Obs_air:

    def __init__(self,serial_number,typee,hub_sn,obs,firmware_revision):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.obs = obs
        self.firmware_revision = firmware_revision

    def unpacker(self,obs):
        timeep = obs[0][0]
        stationpress = obs[0][1]
        airtemp = obs[0][2]
        relhumid = obs[0][3]
        lgtnstrike = obs[0][4]
        lgtnstrikedist_avg = obs[0][5]
        battery = obs[0][6]
        reportint = obs[0][7]
        return timeep, stationpress, airtemp, relhumid, lgtnstrike, lgtnstrikedist_avg, battery, reportint

    def printme(self,timeep, stationpress, airtemp, relhumid, lgtnstrike, lgtnstrikedist_avg, battery, reportint):
        return "THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, Station Pressure: {} MB, Air Temp: {} C, Relative Humidity {} %, LightningStrikeCount {}, Lightning Strike Avg Distance {} Km, Battery {}, Report Interval {} Mins".format(self.serial_number, self.typee, self.hub_sn, timeep, stationpress, airtemp, relhumid, lgtnstrike, lgtnstrikedist_avg, battery, reportint)

class Obs_sky:

    def __init__(self,serial_number,typee,hub_sn,obs,firmware_revision):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.obs = obsstationpress
        self.firmware_revision = firmware_revision

class Device_status:

    def __init__(self,serial_number,typee,hub_sn,timestamp,uptime,
                    voltage,firmware_revision,rssi,sensor_status):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.timestamp = timestamp
        self.uptime = uptime
        self.voltage = voltage
        self.firmware_revision = firmware_revision
        self.rssi = rssi
        self.sensor_status = sensor_status

class Hub_status:

    def __init__(self,serial_number,typee,firmware_revision,uptime,
                    rssi,timestamp,reset_flags,stack,seq,fs):
        self.serial_number = serial_number
        self.typee = typee
        self.firmware_revision = firmware_revision
        self.uptime = uptime
        self.rssi = rssi
        self.timestamp = timestamp
        self.reset_flags = reset_flags
        self.stack = stack
        self.seq = seq
        self.fs = fs
