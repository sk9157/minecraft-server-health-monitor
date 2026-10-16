import subprocess
import socket
import psutil
import csv
from datetime import datetime
import os
import time


def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0


host = "127.0.0.1"
port = 25565
log_file = "server_health.csv"


def check_server():

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    result = subprocess.run(
        ["pgrep", "-f", "server.jar"],
        capture_output=True,
        text=True
    )

    pid = result.stdout.strip()

    port_open = check_port(host, port)


    status = "OFFLINE"
    memory_mb = 0
    cpu_percent = 0

    if pid:
        status = "ONLINE"
        print("Minecraft Server: ONLINE")
        print("PID:", pid)

        process = psutil.Process(int(pid))
        memory_mb = process.memory_info().rss / (1024 * 1024)

        print(f"Memory Usage: {memory_mb:.2f} MB")

        cpu_percent = process.cpu_percent(interval=1)

        print(f"CPU Usage: {cpu_percent:.2f}%")
    else:
        print("Minecraft Server: OFFLINE")

    if port_open:
        print("Port 25565: OPEN")
    else:
        print("Port 25565: CLOSED")



    file_exists = os.path.exists(log_file)

    with open(log_file, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "status",
                "pid",
                "memory_mb",
                "cpu_percent",
                "port_open"
            ])

        writer.writerow([
            timestamp,
            status,
            pid,
            round(memory_mb, 2),
            round(cpu_percent, 2),
            port_open
        ])

print("Minecraft Health Monitor started.")
print("Press Ctrl+C to stop.\n")

while True:
    check_server()
    print("-" * 40)
    time.sleep(30)
