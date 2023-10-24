import asyncio
import socket
import subprocess
import time

import PyOBEX
import bluetooth
from PyOBEX.client import BrowserClient
from PyOBEX.server import Server, BrowserServer
from bleak import BleakClient
import aioconsole

galaxy_buds = "64:03:7F:9D:45:18"
jbl_clip_4 = "F8:5C:7E:3A:D0:9F"

this_device_address = "f8:63:3f:31:38:09"

samsung_phone = "18:4E:16:26:CB:C6"


async def connect():
    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    subprocess.call("kill -9 `pidof bluetooth-agent`", shell=True)
    passcode = "1111"
    subprocess.call("bluetooth-agent " + passcode + " &", shell=True)

    port = 6
    try:
        client_socket.connect((samsung_phone, port))

        # line = await aioconsole.ainput('Is this your line? ')
        print("cos")
        # await task
        print("Connected to phone")

        data_to_send = "Hello, phone!"
        # client_socket.send(data_to_send)

        received_data = client_socket.recv(1024)
        print("Received data: ", received_data.decode('utf-8'))
    except bluetooth.btcommon.BluetoothError as e:
        print("Bluetooth connection error:", e)

    finally:
        client_socket.close()


def main():
    asyncio.run(connect())



if __name__ == '__main__':
    devices = bluetooth.discover_devices()
    for device in devices:
        print("device address: ", device, " name =", bluetooth.lookup_name(device))

    # services = bluetooth.find_service(address=samsung_phone)
    main()

# [{'host': '18:4E:16:26:CB:C6', 'name': None, 'description': '', 'port': 31, 'protocol': 'L2CAP', 'rawrecord': b'6\x000\t\x00\x00\n\x00\x01\x00\x00\t\x00\x015\x03\x19\x18\x01\t\x00\x045\x135\x06\x19\x01\x00\t\x00\x1f5\t\x19\x00\x07\t\x00\x01\t\x00\t\t\x00\x055\x03\x19\x10\x02', 'service-classes': [b'1801'], 'profiles': [], 'provider': None, 'service-id': None, 'handle': 65536}, {'host': '18:4E:16:26:CB:C6', 'name': None, 'description': '', 'port': 31, 'protocol': 'L2CAP', 'rawrecord': b'6\x000\t\x00\x00\n\x00\x01\x00\x01\t\x00\x015\x03\x19\x18\x00\t\x00\x045\x135\x06\x19\x01\x00\t\x00\x1f5\t\x19\x00\x07\t\x00\x14\t\x00\x1a\t\x00\x055\x03\x19\x10\x02', 'service-classes': [b'1800'], 'profiles': [], 'provider': None, 'service-id': None, 'handle': 65537}, {'host': '18:4E:16:26:CB:C6', 'name': b'Advanced Audio Source\x00', 'description': '', 'port': 25, 'protocol': 'L2CAP', 'rawrecord': b'6\x00[\t\x00\x00\n\x00\x01\x00+\t\x00\x015\x03\x19\x11\n\t\x00\x045\x105\x06\x19\x01\x00\t\x00\x195\x06\x19\x00\x19\t\x01\x03\t\x00\x055\x03\x19\x10\x02\t\x00\t5\x085\x06\x19\x11\r\t\x01\x03\t\x01\x00%\x16Advanced Audio Source\x00\t\x03\x11\t\x00\x01', 'service-classes': [b'110a'], 'profiles': [(b'110d', 259)], 'provider': None, 'service-id': None, 'handle': 65579}, {'host': '18:4E:16:26:CB:C6', 'name': b'AV Remote Control\x00', 'description': '', 'port': 23, 'protocol': 'L2CAP', 'rawrecord': b'6\x00Z\t\x00\x00\n\x00\x01\x00-\t\x00\x015\x06\x19\x11\x0e\x19\x11\x0f\t\x00\x045\x105\x06\x19\x01\x00\t\x00\x175\x06\x19\x00\x17\t\x01\x04\t\x00\x055\x03\x19\x10\x02\t\x00\t5\x085\x06\x19\x11\x0e\t\x01\x06\t\x01\x00%\x12AV Remote Control\x00\t\x03\x11\t\x00\x02', 'service-classes': [b'110e', b'110f'], 'profiles': [(b'110e', 262)], 'provider': None, 'service-id': None, 'handle': 65581}, {'host': '18:4E:16:26:CB:C6', 'name': b'AV Remote Control Target\x00', 'description': '', 'port': 23, 'protocol': 'L2CAP', 'rawrecord': b'6\x00\x84\t\x00\x00\n\x00\x01\x00.\t\x00\x015\x03\x19\x11\x0c\t\x00\x045\x105\x06\x19\x01\x00\t\x00\x175\x06\x19\x00\x17\t\x01\x04\t\x00\x055\x03\x19\x10\x02\t\x00\t5\x085\x06\x19\x11\x0e\t\x01\x06\t\x00\r5!5\x105\x06\x19\x01\x00\t\x00\x1b5\x06\x19\x00\x17\t\x01\x045\r5\x06\x19\x01\x00\t\x10\x015\x03\x19\x00\x08\t\x01\x00%\x19AV Remote Control Target\x00\t\x03\x11\t\x01Q', 'service-classes': [b'110c'], 'profiles': [(b'110e', 262)], 'provider': None, 'service-id': None, 'handle': 65582}, {'host': '18:4E:16:26:CB:C6', 'name': b'Headset Gateway\x00', 'description': '', 'port': 3, 'protocol': 'RFCOMM', 'rawrecord': b'6\x00N\t\x00\x00\n\x00\x01\x00/\t\x00\x015\x06\x19\x11\x12\x19\x12\x03\t\x00\x045\x0c5\x03\x19\x01\x005\x05\x19\x00\x03\x08\x03\t\x00\x055\x03\x19\x10\x02\t\x00\t5\x085\x06\x19\x11\x08\t\x01\x02\t\x01\x00%\x10Headset Gateway\x00', 'service-classes': [b'1112', b'1203'], 'profiles': [(b'1108', 258)], 'provider': None, 'service-id': None, 'handle': 65583}, {'host': '18:4E:16:26:CB:C6', 'name': b'Handsfree Gateway\x00', 'description': '', 'port': 4, 'protocol': 'RFCOMM', 'rawrecord': b'6\x00[\t\x00\x00\n\x00\x01\x000\t\x00\x015\x06\x19\x11\x1f\x19\x12\x03\t\x00\x045\x0c5\x03\x19\x01\x005\x05\x19\x00\x03\x08\x04\t\x00\x055\x03\x19\x10\x02\t\x00\t5\x085\x06\x19\x11\x1e\t\x01\x07\t\x01\x00%\x12Handsfree Gateway\x00\t\x03\x01\x08\x01\t\x03\x11\t\x00/', 'service-classes': [b'111f', b'1203'], 'profiles': [(b'111e', 263)], 'provider': None, 'service-id': None, 'handle': 65584}, {'host': '18:4E:16:26:CB:C6', 'name': b'Android Network Access Point\x00', 'description': 'NAP', 'port': 15, 'protocol': 'L2CAP', 'rawrecord': b'6\x00\x8f\t\x00\x00\n\x00\x01\x001\t\x00\x015\x03\x19\x11\x16\t\x00\x045\x185\x06\x19\x01\x00\t\x00\x0f5\x0e\x19\x00\x0f\t\x01\x005\x06\t\x08\x00\t\x08\x06\t\x00\x055\x03\x19\x10\x02\t\x00\x065\t\ten\t\x00j\t\x01\x00\t\x00\t5\x085\x06\x19\x11\x16\t\x01\x00\t\x01\x00%\x1dAndroid Network Access Point\x00\t\x01\x01%\x04NAP\x00\t\x03\n\t\x00\x01\t\x03\x0b\t\x00\x05\t\x03\x0c\n\x00\x13\x12\xd0', 'service-classes': [b'1116'], 'profiles': [(b'1116', 256)], 'provider': None, 'service-id': None, 'handle': 65585}, {'host': '18:4E:16:26:CB:C6', 'name': b'Android Network User\x00', 'description': 'PANU', 'port': 15, 'protocol': 'L2CAP', 'rawrecord': b'6\x00z\t\x00\x00\n\x00\x01\x002\t\x00\x015\x03\x19\x11\x15\t\x00\x045\x185\x06\x19\x01\x00\t\x00\x0f5\x0e\x19\x00\x0f\t\x01\x005\x06\t\x08\x00\t\x08\x06\t\x00\x055\x03\x19\x10\x02\t\x00\x065\t\ten\t\x00j\t\x01\x00\t\x00\t5\x085\x06\x19\x11\x15\t\x01\x00\t\x01\x00%\x15Android Network User\x00\t\x01\x01%\x05PANU\x00\t\x03\n\t\x00\x01', 'service-classes': [b'1115'], 'profiles': [(b'1115', 256)], 'provider': None, 'service-id': None, 'handle': 65586}, {'host': '18:4E:16:26:CB:C6', 'name': b'OBEX Phonebook Access Server\x00', 'description': '', 'port': 19, 'protocol': 'RFCOMM', 'rawrecord': b'6\x00p\t\x00\x00\n\x00\x01\x003\t\x00\x015\x03\x19\x11/\t\x00\x045\x115\x03\x19\x01\x005\x05\x19\x00\x03\x08\x135\x03\x19\x00\x08\t\x00\x055\x03\x19\x10\x02\t\x00\t5\x085\x06\x19\x110\t\x01\x02\t\x01\x00%\x1dOBEX Phonebook Access Server\x00\t\x02\x00\t\x10\x03\t\x03\x14\x08\x0b\t\x03\x17\n\x00\x00\x02\x1f', 'service-classes': [b'112f'], 'profiles': [(b'1130', 258)], 'provider': None, 'service-id': None, 'handle': 65587}, {'host': '18:4E:16:26:CB:C6', 'name': b'OBEX Object Push\x00', 'description': '', 'port': 12, 'protocol': 'RFCOMM', 'rawrecord': b'6\x00j\t\x00\x00\n\x00\x01\x005\t\x00\x015\x03\x19\x11\x05\t\x00\x045\x115\x03\x19\x01\x005\x05\x19\x00\x03\x08\x0c5\x03\x19\x00\x08\t\x00\x055\x03\x19\x10\x02\t\x00\t5\x085\x06\x19\x11\x05\t\x01\x02\t\x01\x00%\x11OBEX Object Push\x00\t\x02\x00\t\x10\x07\t\x03\x035\x0e\x08\x01\x08\x02\x08\x03\x08\x04\x08\x05\x08\x06\x08\xff', 'service-classes': [b'1105'], 'profiles': [(b'1105', 258)], 'provider': None, 'service-id': None, 'handle': 65589}, {'host': '18:4E:16:26:CB:C6', 'name': b'SIM Access\x00', 'description': '', 'port': 6, 'protocol': 'RFCOMM', 'rawrecord': b'6\x00I\t\x00\x00\n\x00\x01\x006\t\x00\x015\x06\x19\x11-\x19\x12\x04\t\x00\x045\x0c5\x03\x19\x01\x005\x05\x19\x00\x03\x08\x06\t\x00\x055\x03\x19\x10\x02\t\x00\t5\x085\x06\x19\x11-\t\x01\x02\t\x01\x00%\x0bSIM Access\x00', 'service-classes': [b'112d', b'1204'], 'profiles': [(b'112d', 258)], 'provider': None, 'service-id': None, 'handle': 65590}, {'host': '18:4E:16:26:CB:C6', 'name': b'SMS/MMS\x00', 'description': '', 'port': 7, 'protocol': 'RFCOMM', 'rawrecord': b'6\x00`\t\x00\x00\n\x00\x01\x007\t\x00\x015\x03\x19\x112\t\x00\x045\x115\x03\x19\x01\x005\x05\x19\x00\x03\x08\x075\x03\x19\x00\x08\t\x00\x055\x03\x19\x10\x02\t\x00\t5\x085\x06\x19\x114\t\x01\x02\t\x01\x00%\x08SMS/MMS\x00\t\x02\x00\t\x10\x05\t\x03\x15\x08\x00\t\x03\x16\x08\x0e\t\x03\x17\n\x00\x00\x00\x7f', 'service-classes': [b'1132'], 'profiles': [(b'1134', 258)], 'provider': None, 'service-id': None, 'handle': 65591}]
