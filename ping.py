import os
import time
import sqlite3
from PyQt5.QtCore import QDateTime

def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "Online"
    else:
        pingstatus = "Offline"
    return pingstatus

def showTime():
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('ss')
        return timeDisplay
    
conn = sqlite3.connect("Content/database/database.db")
cursor = conn.cursor()
cursor.execute("SELECT devices.ip,devices.name,position.ip,position.position FROM devices INNER JOIN position ON devices.name=position.device_name")
ViewData = cursor.fetchall()

while True:
    timecheck = showTime()
    if int(timecheck) % 300 == 0:
        for data in ViewData:
            ping = check_ping(str(data[0]))
            print(data[1] + " IP : " + data[0] + " is " + ping)
            pings = check_ping(str(data[2]))
            print(data[3] + " IP : " + data[2] + " is " + pings)
    time.sleep(1)