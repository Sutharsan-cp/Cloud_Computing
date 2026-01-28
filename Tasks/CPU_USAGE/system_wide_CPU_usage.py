import psutil
import time

def monitor_system_cpu(duration=10, interval=1):
    """
    Monitor overall system CPU usage.
    
    duration: total monitoring time in seconds
    interval: seconds between checks
    """
    for _ in range(duration // interval):
        cpu_usage = psutil.cpu_percent(interval=interval)
        print(f"System CPU usage: {cpu_usage}%")

if __name__ == "__main__":
    print("Monitoring overall system CPU usage...")
    monitor_system_cpu(duration=10, interval=1)
