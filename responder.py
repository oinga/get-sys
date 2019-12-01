import platform
import socket
import re
import uuid
import json
import psutil
from datetime import datetime
# Convert yo exe. with pyinstaller, and install on tablets as bootable?


def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        info['date']=datetime.today().strftime('%Y-%m-%d')
        info['time']=datetime.today().strftime('%H:%M:%S')
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

print(getSystemInfo())
