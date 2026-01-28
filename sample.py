# import psutil
# print("CPU usage (%):", psutil.cpu_percent(interval=1))

# ram = psutil.virtual_memory()
# print("RAM usage (%):", ram.percent)
# print("RAM used (GB):", round(ram.used / 1e9, 2))

# import psutil
# import time
# import os

# def monitor_cpu_usage(pid, interval=1, duration=10):
#     """
#     Monitor CPU usage of a given process.
    
#     pid: process ID of the program to monitor
#     interval: seconds between checks
#     duration: total monitoring time in seconds
#     """
#     process = psutil.Process(pid)
#     for _ in range(duration // interval):
#         cpu_usage = process.cpu_percent(interval=interval)
#         print(f"CPU usage: {cpu_usage}%")

# if __name__ == "__main__":
#     # Example: monitor the current Python process
#     current_pid = os.getpid()
#     print(f"Monitoring CPU usage for PID {current_pid}...")
#     monitor_cpu_usage(current_pid, interval=1, duration=10)

import psutil
import time

for _ in range(10):
    print(f"System CPU usage: {psutil.cpu_percent(interval=1)}%")
