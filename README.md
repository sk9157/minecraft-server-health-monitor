# Minecraft Server Health Monitor

A lightweight Python monitoring tool for tracking the health of a Minecraft Java server running on Ubuntu Linux.

I built this project while learning Linux server administration and wanted a simple way to automatically monitor whether my Minecraft server was running and how many system resources it was using.

## Features

- Detects whether the Minecraft Java server process is online or offline
- Identifies the server process ID (PID)
- Monitors CPU usage
- Monitors memory usage
- Checks whether TCP port 25565 is accepting connections
- Records timestamped health data to a CSV file
- Automatically checks server health every 30 seconds
- Detects server shutdowns and restarts

## Example Output

```text
Minecraft Server: ONLINE
PID: 2011
Memory Usage: 990.95 MB
CPU Usage: 2.00%
Port 25565: OPEN
----------------------------------------
Minecraft Server: OFFLINE
Port 25565: CLOSED
----------------------------------------
Minecraft Server: ONLINE
PID: 2090
Memory Usage: 987.48 MB
CPU Usage: 6.00%
Port 25565: OPEN
```

The change in PID from `2011` to `2090` shows the monitor detecting the server shutting down and later starting again as a new process.

## Technologies

- Python
- Linux (Ubuntu Server)
- psutil
- Python socket API
- SSH
- Java / Minecraft Server

## How It Works

The monitor searches for the Minecraft `server.jar` process and uses its PID to collect CPU and memory usage.

It also attempts a TCP connection to port `25565`, the default Minecraft Java server port, to verify that the server is accepting connections.

Each health check is written to a CSV file with:

- Timestamp
- Online/offline status
- PID
- Memory usage
- CPU usage
- Port status

The monitor repeats the health check every 30 seconds until stopped by the user.

## What I Learned

This project gave me hands-on experience with:

- Installing and managing an Ubuntu Linux server
- Using SSH for remote server administration
- Managing packages and Java runtimes on Linux
- Inspecting Linux processes and network sockets
- Troubleshooting Java runtime compatibility
- Using Python to interact with operating system processes
- Using TCP sockets to test service availability
- Logging system health data for later analysis

During setup, I encountered a Java class-version compatibility error when the Minecraft server required a newer Java runtime. I identified the version mismatch, installed the appropriate OpenJDK runtime, and verified that the server process was successfully listening on TCP port 25565.

## Future Improvements

Possible improvements include:

- Configurable monitoring intervals
- Alerts when the server goes offline
- Historical CPU and memory visualizations
- Monitoring player count and server uptime
- Running the monitor as a Linux system service
