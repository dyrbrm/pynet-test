#!/usr/bin/env python

import snmp_helper

ip_addr = '50.76.53.27'
COMMUNITY_STRING = 'galileo'
SNMP_PORT = [7961, 8061]
sysDescr = '1.3.6.1.2.1.1.1.0'
sysName = '1.3.6.1.2.1.1.5.0'

def snmpget(device,oid):
    snmp_data = snmp_helper.snmp_get_oid(device,oid)
    output = snmp_helper.snmp_extract(snmp_data)
    return output

def main():
    for port in SNMP_PORT:
        device = (ip_addr, COMMUNITY_STRING, port)
        print snmpget(device,sysDescr)
        print snmpget(device,sysName)

if  __name__ == '__main__':
    main()
