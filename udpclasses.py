import numpy as np
import pandas as pd

#This file is a translation to Python of enum.ts

class Evt_precip:

    def __init__(self,serial_number,typee,hub_sn,evt):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.evt = evt
        self.unpacker()
        self.printme()

    def unpacker(self):
        self.timeep = self.evt[0]

    def printme(self):
        #return "THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {}".format(self.serial_number, self.typee, self.hub_sn, time_epoch)
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {}".format(self.serial_number, self.typee, self.hub_sn, self.timeep))

class Evt_strike:

    def __init__(self,serial_number,typee,hub_sn,evt):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.evt = evt
        self.unpacker()
        self.printme()

    def unpacker(self):
        self.timeep = self.evt[0]
        self.Distance = self.evt[1]
        self.Energy = self.evt[2]

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, Distance: {} meters, Energy: {}".format(self.serial_number, self.typee, self.hub_sn, self.timeep, self.Distance, self.Energy))

class Rapid_wind:

    def __init__(self,serial_number,typee,hub_sn,ob):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.ob = ob
        self.unpacker()
        self.transform_winddir()
        self.printme()

    def unpacker(self):
        self.timeep = self.ob[0]
        self.windspeed = self.ob[1]
        self.winddirn = self.ob[2]

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, WindSpeed: {} m/sec, WindDirection: {} Degrees".format(self.serial_number, self.typee, self.hub_sn, self.timeep, self.windspeed, self.winddirn))
    #Wind Direction has been flipped by 180Degrees because the weatherflow tempest unit was designed in the Northern
    #Hemisphere and we are using this device in the Southern Hemisphere.
    def transform_winddir(self):
        if self.winddirn > 180:
            self.winddirn = self.winddirn - 180
        elif self.winddirn < 180:
            self.winddirn = self.winddirn + 180
        elif self.winddirn == 0 or self.winddirn == 360:
            self.winddirn == 180
        elif self.winddirn == 180:
            self.winddirn == 0

class Obs_air:

    def __init__(self,serial_number,typee,hub_sn,obs,firmware_revision):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.obs = obs
        self.firmware_revision = firmware_revision
        self.unpacker()
        self.printme()

    def unpacker(self):
        self.timeep = self.obs[0][0]
        self.stationpress = self.obs[0][1]
        self.airtemp = self.obs[0][2]
        self.relhumid = self.obs[0][3]
        self.lgtnstrike = self.obs[0][4]
        self.lgtnstrikedist_avg = self.obs[0][5]
        self.battery = self.obs[0][6]
        self.reportint = self.obs[0][7]
        
    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, Station Pressure: {} MB, Air Temp: {} C, Relative Humidity {} %, LightningStrikeCount {}, Lightning Strike Avg Distance {} Km, Battery {}, Report Interval {} Mins, Firmware Rev: {}".format(self.serial_number, self.typee, self.hub_sn, self.timeep, self.stationpress, self.airtemp, self.relhumid, self.lgtnstrike, self.lgtnstrikedist_avg, self.battery, self.reportint, self.firmware_revision))

class Obs_sky:

    def __init__(self,serial_number,typee,hub_sn,obs,firmware_revision):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.obs = obs
        self.firmware_revision = firmware_revision
        self.unpacker()
        self.transform_winddir()
        self.printme()

    def unpacker(self):
        self.timeep = self.obs[0][0]
        self.illum = self.obs[0][1]
        self.ultravio = self.obs[0][2]
        self.rainAccum = self.obs[0][3]
        self.windLull = self.obs[0][4]
        self.windAvg = self.obs[0][5]
        self.windGust = self.obs[0][6]
        self.windDir = self.obs[0][7]
        self.battery = self.obs[0][8]
        self.reportint = self.obs[0][9]
        self.solarRad = self.obs[0][10]
        self.locrainAccum = self.obs[0][11]
        self.precipType = self.obs[0][12]
        self.windSampInt = self.obs[0][13]

    #Wind Direction has been flipped by 180Degrees because the weatherflow tempest unit was designed in the Northern
    #Hemisphere and we are using this device in the Southern Hemisphere.
    def transform_winddir(self):
        if self.windDir > 180:
            self.windDir = self.windDir - 180
        elif self.windDir < 180:
            self.windDir = self.windDir + 180
        elif self.windDir == 0 or self.windDir == 360:
            self.windDir == 180
        elif self.windDir == 180:
            self.windDir == 0

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_epoch: {} seconds, Illumination: {} Lux, UltraViolet: {} Index, Rain Accumulated: {} mm, Wind Lull: {} m/s, Wind Avg: {} m/s, Wind Gust: {} m/s, Wind Direction: {} Degrees, Battery: {} Volts, Report Interval: {} Minutes, Solar Radiation: {} W/m2, Local Day Rain Accumulation: {} mm, Precipitation Type: {}, Wind Sample Interval: {} secs, Firmware Version: {}".format(self.serial_number, self.typee, self.hub_sn, self.timeep, self.illum, self.ultravio, self.rainAccum, self.windLull, self.windAvg, self.windGust, self.windDir, self.battery, self.reportint, self.solarRad, self.locrainAccum, self.precipType, self.windSampInt, self.firmware_revision))

class Device_status:

    def __init__(self, serial_number, typee, hub_sn, timestamp, uptime,
                    voltage, firmware_revision, rssi, hub_rssi, sensor_status, debug):
        self.serial_number = serial_number
        self.typee = typee
        self.hub_sn = hub_sn
        self.timestamp = timestamp
        self.uptime = uptime
        self.voltage = voltage
        self.firmware_revision = firmware_revision
        self.rssi = rssi
        self.hub_rssi = hub_rssi
        self.sensor_status = sensor_status
        self.debug = debug
        self.printme()

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, hub_sn: {}, time_stamp: {} seconds, Uptime: {} Secs, Voltage: {} Volts, Firmware Rev: {}, RSSI: {}, HUB_RSSI: {}, Sensor Status: {}, Debug Flag: {}".format(self.serial_number, self.typee, self.hub_sn, self.timestamp, self.uptime, self.voltage, self.firmware_revision, self.rssi, self.hub_rssi, self.sensor_status, self.debug))


class Hub_status:

    def __init__(self, serialnum, typee, uptime,rssi, timestamp, resetflags, seq, fs,
                                radiostats, mqttstats):
        self.serialnum = serialnum
        self.typee = typee
        self.uptime = uptime
        self.rssi = rssi
        self.timestamp = timestamp
        self.resetflags = resetflags
        self.seq = seq
        self.fs = fs
        self.radiostats = radiostats
        self.mqttstats = mqttstats
        self.printme()

    def printme(self):
        print("THE UNPACKED VALUES ARE: Serial_Number: {}, type: {}, Up Time: {} Seconds, RSSI: {}, Time Stamp: {} Secs, Reset Flags: {}, Seq: {}, FS: {}, Radio Stats: {}, MQTT STATS: {}".format(self.serialnum, self.typee, self.uptime, self.rssi, self.timestamp, self.resetflags, self.seq, self.fs, self.radiostats, self.mqttstats))
