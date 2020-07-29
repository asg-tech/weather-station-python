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

class Obs_sky:

    def __init__(self,serial_number,typee,hub_sn,obs,firmware_revision):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.obs = obs
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
