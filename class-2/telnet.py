#!/usr/bin/env python

import telnetlib
import time
import sys
import socket

TELNET_PORT = 23
TELNET_TIMEOUT = 10

def connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed out!")

def login(conn, username, password):
    output = conn.read_until('sername:', TELNET_TIMEOUT)
    conn.write(username + '\n')
    output += conn.read_until('assword:', TELNET_TIMEOUT)
    conn.write(password + '\n')
    return output

def command(conn, cmd=''):
    conn.write(cmd + '\n')
    time.sleep(1)
    output = conn.read_very_eager()
    return output

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'

    conn = connect(ip_addr)
    output = login(conn, username, password)
    output += command(conn, 'terminal length 0')
    output += command(conn, 'show ip int brief')

    print output

    conn.close()

if __name__ == '__main__':
    main()
