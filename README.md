# 🖥️ Server Monitor

**Lightweight Linux server monitoring tool written in Python.**

Server Monitor is a simple terminal utility for quickly checking the current state of a Linux server.

## ✨ Features

* 🧠 CPU usage monitoring
* 💾 RAM usage monitoring
* 💿 Disk usage monitoring
* ⏱️ Server uptime
* 🌐 Internet connectivity check
* 🔌 TCP port monitoring
* 🚦 Automatic server health status

## 🚦 Status Levels

The application automatically evaluates CPU, RAM and disk usage.

| Status          | Meaning                                                  |
| --------------- | -------------------------------------------------------- |
| 🟢 **OK**        | Resource usage is within normal limits                   |
| 🟡 **WARNING**  | Resource usage is high and should be monitored            |
| 🔴 **CRITICAL** | Resource usage is critically high and may require action |

### What does `WARNING` mean?

`WARNING` does **not** mean that the server is broken or that a rocket is flying into it. 🚀

It simply means that one of the monitored resources has exceeded the warning threshold.

For example:

```text
CPU:       74.2%   WARNING
```

This means that CPU usage is relatively high, but the server can continue working normally.

---

## 📊 Example of the Application

This is an example of what the program looks like when running:

```text
=============================================
          SERVER MONITOR
=============================================

SYSTEM
---------------------------------------------
CPU:       34.2%   OK
RAM:       76.4%   WARNING
DISK:      41.7%   OK
UPTIME:     4d 12h 31m
STATUS:   WARNING

NETWORK
---------------------------------------------
Internet: ONLINE

PORTS
---------------------------------------------
22     SSH      OPEN
80     HTTP     OPEN
443    HTTPS    CLOSED
3000   App      CLOSED

=============================================
```

The monitor checks the server and displays the results directly in the terminal.

---

## 🛠️ Technologies

* Python 3
* psutil
* Linux
* Git
* GitHub

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Codedbybro/server-monitor.git
cd server-monitor
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the dependency:

```bash
pip install psutil
```

Run the monitor:

```bash
python3 monitor.py
```

## 📁 Project Structure

```text
server-monitor/
├── monitor.py
├── .gitignore
└── README.md
```

## 📌 Project Status

This is an educational DevOps/Python project created to practice:

* Python
* Linux
* Networking
* Git
* GitHub
* Server monitoring

The project is actively being developed and will receive additional monitoring features in future versions.


