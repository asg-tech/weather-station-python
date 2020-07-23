import numpy as np
import pandas as pd

#This file is a translation to Python of enum.ts

class Evt_precip:
    def __init__(self,serial_number,typee,hub_sn,evt):

        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.evt = evt

    def doEvtPrecip(self):
        return "This is the event: " + str(self.evt)

class Evt_strike:
    def __init__(self,serial_number,typee,hub_sn,evt):

        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.evt = evt

class Rapid_wind:
    def __init__(self,serial_number,typee,hub_sn,ob):

        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.ob = ob

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
