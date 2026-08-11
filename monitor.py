import os
import socket
import time
import psutil


def get_cpu():
    return psutil.cpu_percent(interval=1)


def get_memory():
    memory = psutil.virtual_memory()
    return memory.percent


def get_disk():
    disk = psutil.disk_usage("/")
    return disk.percent


def get_status(value, warning=70, critical=90):
    if value >= critical:
       return "CRITICAL"
    elif value >= warning:
         return "WARNING"
    else:
         return "OK"


def get_overall_status(cpu, ram, disk):
    statuses = [
        get_status(cpu),
        get_status(ram),
        get_status(disk)
    ]
    if "CRITICAL" in statuses:
        return "CRITICAL"
    elif "WARNING" in statuses:
        return "WARNING"
    else:
        return "OK"


def get_uptime():
    uptime = time.time() - psutil.boot_time()

    days = int(uptime // 86400)
    hours = int((uptime % 86400) // 3600)
    minutes = int((uptime % 3600) // 60)

    return f"{days}d {hours}h {minutes}m"


def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False


def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        result = sock.connect_ex((host, port))

        if result == 0:
            return True

        return False

    finally:
        sock.close()


def main():
    print("=" * 45)
    print("          SERVER MONITOR")
    print("=" * 45)

    print("\nSYSTEM")
    print("-" * 45)

    cpu = get_cpu()
    ram = get_memory()
    disk = get_disk()
  
    overall_status = get_overall_status(cpu, ram, disk)
 
    print(f"CPU:      {cpu:6.1}% {get_status(cpu)}")
    print(f"RAM:      {ram:>6.1f}% {get_status(ram)}")
    print(f"DISK:     {disk:>6.1f}% {get_status(disk)}")
    print(f"UPTIME:   {get_uptime()}")
    print(f"STATUS:   {overall_status}")


    print("\nNETWORK")
    print("-" * 45)

    internet = check_internet()

    if internet:
        print("Internet: ONLINE")
    else:
        print("Internet: OFFLINE")

    print("\nPORTS")
    print("-" * 45)

    ports = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3000: "App",
    }

    for port, name in ports.items():
        if check_port("127.0.0.1", port):
            print(f"{port:<6} {name:<8} OPEN")
        else:
            print(f"{port:<6} {name:<8} CLOSED")

    print("\n" + "=" * 45)


if __name__ == "__main__":
    main()
