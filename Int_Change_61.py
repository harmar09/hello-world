from cli import *

cli("conf ; int e1/2 ; no switchport; ip address 192.168.61.1/24 ; no shut")
cli("conf ; vlan 1005")
cli("conf ; int e1/3 ; switchport; switchport access vlan 1005 ; no shut")
clip("show run int e1/2")
raw_input('press Enter to continue')
clip("show run int e1/3")
raw_input('press Enter to continue')
clip("show run int brief")
raw_input('press Enter to continue')
clip("show ip int brief")
