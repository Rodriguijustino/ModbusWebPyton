#pip install pyModbusTCP
#https://pypi.org/project/pyModbusTCP/
from pyModbusTCP.client import ModbusClient

#pip install requests
#https://pypi.org/project/requests/
import requests

import time

clp41 = ModbusClient(host="192.168.10.41", port=502, unit_id=1, auto_open=True)

#status = []

while True:
    res = requests.get('https://gitintechgooglesitesrender.onrender.com')
    response = res.json()
    print(response)

    clp41.write_single_coil(0, response["l1"])

    #clp41.write_multiple_coils(0,status[0,1,0,1,1])
    time.sleep(0.01)

#pm2 start index.py --interpreter python3