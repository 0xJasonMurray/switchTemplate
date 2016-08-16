# Using Python and Jinja2 Templates to Configure Network Devices

## Overview
This repository contains basic examples on how to use Python and Jinja2 to
configure network switches using template based configurations.

In 2016 we needed to configure 100+ standard network access switches for a large
event.  The basic template was simple:

* Unique hostname for all switches
* Unique /32 point-to-point address
* 2x routed point-to-point interfaces (dual-homed)
* Basic EIGRP configuration
* Any number of switch ports
* Script input comes from CSV file
* All switches should be based on the same configuration
* No manual configure necessary, everything should come from the template
* Each switch configuration is contained in it's own file
* Also output the configuration necessary to configure Infoblox using IBCLI:
  * Create subnet
  * Create DHCP pools (with proper options)
  * Add all DNS entires for P2P and Lo0 interfaces

## Files
* switch-template.py - Main script
* input.csv - Input file in the following format (hostname, lo0, p2p-1-ip, p2p-1-mask, p2p-2-ip, p2p-2-mask, access-gateway, access-mask, number-of-switch-ports)
* templates/switch.tmpl - basic Cisco switch template (Example only, don't use in production, it probably contains errors)
* templates/infoblox.tmpl - Infoblox IBCLI template for building subnets, dhcp scopes, and host entries.  
* hostname-\* - Example output for processed switch configurations.
* infoblox-ibcli.txt - Example output for Infoblox IBCLI


