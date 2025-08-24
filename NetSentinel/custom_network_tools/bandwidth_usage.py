import psutil
import time
import os

size = ['bytes', 'KB', 'MB', 'GB', 'TB']

netStats1 = psutil.net_io_counters()

def getSize(bytes):
    for unit in size:
        if bytes < 1024:
            return f"{bytes:.1f}{unit}"
        bytes /= 1024

while True:
    time.sleep(1)
    
    os.system('cls')
    
    netStats2 = psutil.net_io_counters()
    
    dataSent = netStats1.bytes_sent
    dataRecv = netStats1.bytes_recv
    
    uploadStat = netStats2.bytes_sent - dataSent
    downloadStat = netStats2.bytes_recv - dataRecv

    print(f"Data sent: {getSize(dataSent)}")
    print(f"Data receive: {getSize(dataRecv)}")
    
    print(f"Data sending: {getSize(uploadStat)}")
    print(f"Data receiving: {getSize(downloadStat)}")