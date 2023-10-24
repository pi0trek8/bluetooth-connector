import asyncio
import time

import bluetooth
from bleak import BleakScanner, BleakClient


async def main():
    devices = await BleakScanner.discover(10)
    for device in devices:
        print(device, device.details)
    # address = "F6:2E:71:DC:68:FB"
    # address2 = "C8:58:C0:B9:03:3D"
    # address3 = "3C:86:3B:D4:D1:F2"
    # async with BleakClient(address3) as client:
    #     print("Connected")
    #     time.sleep(10)
asyncio.run(main())