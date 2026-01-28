import psutil
import os
import time

def monitor_process_cpu(pid, duration=5, interval=1):
    """
    Monitor CPU usage of a specific process.
    pid: process ID of the program to monitor
    duration: total monitoring time in seconds
    interval: seconds between checks
    """
    process = psutil.Process(pid)

    # Prime the measurement (first call sets baseline)
    process.cpu_percent(interval=None)

    for _ in range(duration // interval):
        cpu_usage = process.cpu_percent(interval=interval)
        print(f"Process CPU usage: {cpu_usage}%")

# Example workload to generate CPU activity
def heavy_task():
    total = 0
    for i in range(10**7):
        total += i
    return total

if __name__ == "__main__":
    current_pid = os.getpid()
    print(f"Monitoring CPU usage for Python process PID {current_pid}...")

    # Start monitoring in parallel with workload
    from threading import Thread
    monitor_thread = Thread(target=monitor_process_cpu, args=(current_pid, 5, 1))
    monitor_thread.start()

    # Run workload
    heavy_task()

    monitor_thread.join()
