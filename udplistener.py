#This file is a translation to Python of server.ts
import udpclasses

def runthis():
    fedclass = udpclasses.Evt_precip("first val","Thanks Glenn",3,4)
    print(fedclass.serial_number, fedclass.typee, fedclass.evt, fedclass.hub_sn)
    print(fedclass.doEvtPrecip())
runthis()