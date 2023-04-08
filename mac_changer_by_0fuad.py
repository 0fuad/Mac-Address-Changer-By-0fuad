import subprocess
from optparse import OptionParser
import re

def user_inputs():
    print( "Mac Address Changer started..." )
    parser = OptionParser()
    parser.add_option("-i" , "--interface" , dest="interface" , help="Enter here your interface(eth0,eth1)" )
    parser.add_option("-m" , "--macaddress" , dest="mac_address" , help="Enter here your new MAC address(AA:BB:CC:DD:EE:FF)" )
    return  parser.parse_args()

def check_inputs(interface,mac_address):
    if not interface:
        interface = input( "Enter your interface: " )
    if not mac_address:
        mac_address = input( "Enter your new MAC Address: " )
    return interface , mac_address

def mac_changer( interface , mac_address ):
    subprocess.call([ "ifconfig" , interface , "down" ])
    subprocess.call([ "ifconfig" , interface , "hw" , "ether" , mac_address ])
    subprocess.call([ "ifconfig" , interface , "up" ])

def check_mac_address(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    ifconfig_str = ifconfig.decode()
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_str)
    if new_mac:
        return new_mac.group(0)
    else:
        print("Something went wrong1")
        return False

print("""""
███    ███  █████   ██████      ██████ ██   ██  █████  ███    ██  ██████  ███████ ██████
████  ████ ██   ██ ██          ██      ██   ██ ██   ██ ████   ██ ██       ██      ██   ██
██ ████ ██ ███████ ██          ██      ███████ ███████ ██ ██  ██ ██   ███ █████   ██████
██  ██  ██ ██   ██ ██          ██      ██   ██ ██   ██ ██  ██ ██ ██    ██ ██      ██   ██
██      ██ ██   ██  ██████      ██████ ██   ██ ██   ██ ██   ████  ██████  ███████ ██   ██

By Fuad Aghayev [0fuad]""")

(usr_inputs , arg) = user_inputs()
interface , mac_address = check_inputs(usr_inputs.interface , usr_inputs.mac_address)
mac_changer(interface,mac_address)
final_mac_address = check_mac_address(interface)
if final_mac_address == mac_address:
    print("Mac Address Successfully Changed")
else:
    print("Something went wrong")