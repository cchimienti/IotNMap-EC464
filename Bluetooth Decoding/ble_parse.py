#!/usr/bin/env python
# parse bletxt into AdvA & Data Manufacturer

#Where can I find the list of registered company IDs which are set right 
#after the AD type field in an AD Structure in a BLE advertising packet when the AD type is 0xFF (Manufacturer Specific Data)?

import re
text = open('BLE2.txt', 'r') 
lines = text.readlines()

device = {}
# from https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers
facturers = {'4C': 'Apple Inc.', 
             '06': 'Microsoft',
             '08': 'Motorola',
             '0D': 'Texas Instruments Inc.',
             'E0': 'Google'}

for l in lines:
    sep = l.split(' ')
    for part in sep:
        if part.startswith("AdvA"):
            MAC = part
            MAC = re.sub("AdvA:", '', MAC)
        elif part.startswith("Data"):
            Manufact = part
            Manufact = re.sub("Data:", '', Manufact)
            if Manufact is not None:
                try: 
                    m1, Manufact = Manufact.split('ff', 1)
                    device.update({MAC: Manufact[:2]})
                except:
                    #skip
                    pass
#print(device)

# find manufacturer based on value and replace in dict:
for k, v in device.items():
    #convert to upper case to match manufacturers dictionary
    v = v.upper()
    newman = facturers[v]
    device.update({k: newman})
print(device)