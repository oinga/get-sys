from flask import Flask
from flask import render_template
import psutil
import platform
import os
from datetime import datetime

app = Flask(__name__)

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

@app.route('/')
def index():
    uname = platform.uname()
    boot_time_timestamp = psutil.boot_time()
    svmem = psutil.virtual_memory()
    cpufreq = psutil.cpu_freq()
    system = uname.system
    node_name = uname.node
    release = uname.release
    version = uname.version
    machine = uname.machine
    processor = uname.processor
    bt = datetime.fromtimestamp(boot_time_timestamp)
    boot_time = """Date: {}-{}-{}  Time: {}:{}:{}""".format(
                                                bt.year,
                                                bt.month,
                                                bt.day,
                                                bt.hour,
                                                bt.minute,
                                                bt.second)
    physical_cores = psutil.cpu_count(logical=False)
    total_cores = psutil.cpu_count(logical=True)
    cpu_max = cpufreq.max
    cpu_min = cpufreq.min
    cpu_current = cpufreq.current
    cpu_usage = psutil.cpu_percent()
    total_memory = get_size(svmem.total)
    return render_template('index.html',
                            system=system,
                            node_name=node_name,
                            release=release,
                            version=version,
                            machine=machine,
                            processor=processor,
                            boot_time=boot_time,
                            physical_cores=physical_cores,
                            total_cores=total_cores,
                            cpu_max=cpu_max,
                            cpu_min=cpu_min,
                            cpu_current=cpu_current,
                            cpu_usage=cpu_usage,
                            total_memory=total_memory)




if __name__ == '__main__':
    app.run(debug=True)
