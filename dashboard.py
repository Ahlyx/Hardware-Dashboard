import psutil
import platform
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import time

console = Console()
#gets system info and formats output
def get_system_info():
    table = Table(title="System")
    table.add_column("Property", style="cyan")
    table.add_column("Values", style="white")

    table.add_row("OS", platform.system())
    table.add_row("OS Version", platform.version())
    table.add_row("Architecture", platform.architecture()[0])
    table.add_row("Hostname", platform.node())
    table.add_row("Processor", platform.processor())

    return table

#gets cpu info and formats output
def get_cpu_info():
    table = Table(title = "CPU")
    table.add_column("Property", style = "cyan")
    table.add_column("Values", style = "white")

    table.add_row("Physical Cores", str(psutil.cpu_count(logical = False)))
    table.add_row("Total Cores", str(psutil.cpu_count(logical = True))) #logical cores from hyperthreading
    table.add_row("Current Speed", f"{psutil.cpu_freq().current:.2f} MHz")
    table.add_row("CPU Usage", f"{psutil.cpu_percent(interval = 1)}%")

    return table
#gets ram and swap memory info, converts bytes to GBs and formats output
def get_ram_info():
    ram = psutil.virtual_memory()
    swap = psutil.swap_memory()
    table = Table(title = "Ram")
    table.add_column("Property", style = "cyan")
    table.add_column("Values", style = "white")
    
    table.add_row("Total", f"{ram.total / 1024 ** 3:.2f} GB")
    table.add_row("Used", f"{ram.used / 1024 ** 3:.2f} GB")
    table.add_row("Available", f"{ram.available / 1024 ** 3:.2f} GB")
    table.add_row("Usage", f"{ram.percent}%")
    table.add_row("Swap Total", f"{swap.total / 1024 ** 3:.2f} GB")
    table.add_row("Swap Used", f"{swap.used / 1024 ** 3:.2f} GB")
    table.add_row("Swap Usage", f"{swap.percent}%")
    return table
#loops through disks and accesses each mountpoint, formats output
def get_disk_info():
    io = psutil.disk_io_counters()

    table = Table(title = "Disks")
    table.add_column("Property", style = "cyan")
    table.add_column("Values", style = "white")

    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        table.add_row("Mountpoint", partition.mountpoint)
        table.add_row("Filesystem", partition.fstype)
        table.add_row("Total", f"{usage.total / 1024 ** 3:.2f} GB")
        table.add_row("Used", f"{usage.used / 1024 ** 3:.2f} GB")
        table.add_row("Free", f"{usage.free / 1024 ** 3:.2f} GB")
        table.add_row("Usage", f"{usage.percent}%")
    
    table.add_row("Total Read", f"{io.read_bytes / 1024 ** 3:.2f} GB")
    table.add_row("Total Written", f"{io.write_bytes / 1024 ** 3:.2f} GB")
    table.add_row("Read Operations", str(io.read_count))
    table.add_row("Write Operations", str(io.write_count))

    return table
#gets ipv4 info and formats output
def get_network_info():
    io = psutil.net_io_counters()
    
    table = Table(title="Network")
    table.add_column("Property", style="cyan")
    table.add_column("Values", style="white")

    for interface_name, addresses in psutil.net_if_addrs().items():
        for address in addresses:
            if str(address.family) == "AddressFamily.AF_INET": #IPv4 only
                table.add_row("Interface", interface_name)
                table.add_row("IP Address", address.address)
                table.add_row("Subnet Mask", address.netmask)

    table.add_row("Bytes Sent", f"{io.bytes_sent / 1024**2:.2f} MB")
    table.add_row("Bytes Received", f"{io.bytes_recv / 1024**2:.2f} MB")
    table.add_row("Packets Sent", str(io.packets_sent))
    table.add_row("Packets Received", str(io.packets_recv))

    return table

#Menu to see desired output
def menu():
    console.print("[cyan]Hardware Dashboard[/cyan]")
    console.print("1. System Info")
    console.print("2. CPU")
    console.print("3. RAM")
    console.print("4. Disk")
    console.print("5. Network")
    console.print("6. Exit")
    return input("Select a section: ")
#Calls functions and refreshes periodically for updated info
try:
    while True:
        console.clear()
        choice = menu()
        console.clear()
        if choice == "1":
            console.print(Panel(get_system_info()))
            input("\nPress Enter to return to menu...")
        elif choice == "2":
            try:
                while True:
                    console.clear()
                    console.print(Panel(get_cpu_info()))
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
        elif choice == "3":
            try:
                while True:
                    console.clear()
                    console.print(Panel(get_ram_info()))
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
        elif choice == "4":
            console.print(Panel(get_disk_info()))
            input("\nPress Enter to return to menu...")
        elif choice == "5":
            try:
                while True:
                    console.clear()
                    console.print(Panel(get_network_info()))
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
        elif choice == "6":
            break
        else:
            console.print("[bold red]Invalid option, please enter a number 1-6[/bold red]")
            input("\nPress Enter to return to menu...")
except KeyboardInterrupt:
    console.print("[cyan]Dashboard closed.[/cyan]")

