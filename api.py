import psutil
import platform
import socket
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/api/system")
def system():
    return {
    "os" : platform.system(),
    "os_version" : platform.version(),
    "architecture" : platform.architecture()[0],
    "hostname" : platform.node(),
    "processor" : platform.processor()
    }

@app.get("/api/cpu")
def cpu():
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "current_speed": f"{psutil.cpu_freq().current:.2f} MHz",
        "cpu_usage": f"{psutil.cpu_percent(interval=1)}%"
    }

@app.get("/api/ram")
def ram():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return{
        "total": f"{mem.total / 1024**3:.2f} GB",
        "used": f"{mem.used / 1024**3:.2f} GB",
        "available": f"{mem.available / 1024**3:.2f} GB",
        "usage": f"{mem.percent}%",
        "swap_total": f"{swap.total / 1024**3:.2f} GB",
        "swap_used": f"{swap.used / 1024**3:.2f} GB",
        "swap_usage": f"{swap.percent}%"
    }

@app.get("/api/disk")
def disk():
    io = psutil.disk_io_counters()
    partitions = []
    
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        partitions.append({
            "mountpoint": partition.mountpoint,
            "filesystem": partition.fstype,
            "total": f"{usage.total / 1024**3:.2f} GB",
            "used": f"{usage.used / 1024**3:.2f} GB",
            "free": f"{usage.free / 1024**3:.2f} GB",
            "usage": f"{usage.percent}%"
        })
    
    return {
        "partitions": partitions,
        "total_read": f"{io.read_bytes / 1024**3:.2f} GB",
        "total_written": f"{io.write_bytes / 1024**3:.2f} GB",
        "read_ops": str(io.read_count),
        "write_ops": str(io.write_count)
    }

@app.get("/api/network")
def network():
    io = psutil.net_io_counters()
    interfaces = []

    for interface_name, addresses in psutil.net_if_addrs().items():
        for address in addresses:
            if address.family == socket.AF_INET: 
                interfaces.append({
                "interface" : interface_name,
                "ip_address" : address.address,
                "subnet_mask" : address.netmask
            })
    
    return {
    "interfaces": interfaces,
    "bytes_sent" : f"{io.bytes_sent / 1024 ** 2:.2f} MB",
    "bytes_received" : f"{io.bytes_recv / 1024 ** 2:.2f} MB",
    "packets_sent" : io.packets_sent,
    "packets_received" : io.packets_recv
    }