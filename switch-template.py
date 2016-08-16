#!/usr/bin/python

import re
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
switch_template = env.get_template('switch.tmpl')
infoblox_template = env.get_template('infoblox.tmpl')

listofswitches = open('input.csv', 'r')
ifd = open("infoblox-ibcli.txt", 'a')

for line in listofswitches:
    hostname = line.split(',')[0]
    lo0 = line.split(',')[1]
    p2p1ip = line.split(',')[2]
    p2p1mask = line.split(',')[3]
    p2p2ip = line.split(',')[4]
    p2p2mask = line.split(',')[5]
    accessgw = line.split(',')[6]
    accessmask = line.split(',')[7]
    switchports = int(line.split(',')[8])+1

    # The CSV contains the access VLAN gateway IP, group(2) contains the first 3 octets.
    result = re.match('^\s*(([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\.[0-9]{1,3})$', accessgw)
    if result:
        networkid = result.group(2)

# Uncomment this to print to screen
#    print switch_template.render(hostname=hostname, lo0=lo0, p2p1ip=p2p1ip,
#                                 p2p1mask=p2p1mask, p2p2ip=p2p2ip,
#                                 p2p2mask=p2p2mask, accessgw=accessgw,
#                                 accessmask=accessmask, switchports=switchports)

    sfd = open(hostname, 'w')
    sfd.write(switch_template.render(hostname=hostname, lo0=lo0, p2p1ip=p2p1ip,
                                     p2p1mask=p2p1mask, p2p2ip=p2p2ip,
                                     p2p2mask=p2p2mask, accessgw=accessgw,
                                     accessmask=accessmask, switchports=switchports))

    sfd.close()

# Uncomment this to print to screen
#    print infoblox_template.render(hostname=hostname, networkid=networkid,
#                                   accessgw=accessgw, lo0=lo0)
    ifd.write(infoblox_template.render(hostname=hostname, networkid=networkid,
                                       accessgw=accessgw, lo0=lo0))

ifd.close()
