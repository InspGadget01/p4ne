from pysnmp.hlapi import *

obj_ver = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)  # По имени MIB-переменной


result = (getCmd(SnmpEngine(),
                 CommunityData("public", mpModel=0),
                 UdpTransportTarget(("10.31.70.209", 161)),
                 ContextData(),
                 ObjectType(obj_ver))),


result2 = nextCmd(SnmpEngine(),
                  CommunityData('public', mpModel=0),
                  UdpTransportTarget(('10.31.70.107', 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
                  lexicographicMode=False)

for received_data in result:
    for x in received_data[3]:
        print(x)

for received_data in result2:
    for x in received_data[3]:
        print(x)
