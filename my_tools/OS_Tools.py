import GPUtil
import psutil
import shutil
from tabulate import tabulate

def get_gpu_usage():
    """Get GPU usage statistics."""
    gpus = GPUtil.getGPUs()
    gpu_data = []
    for gpu in gpus:
        gpu_data.append({
            "GPU ID": gpu.id,
            "Memory Free": f"{gpu.memoryFree} MB",
            "Memory Used": f"{gpu.memoryUsed} MB",
            "Memory Total": f"{gpu.memoryTotal} MB",
            "GPU Load": f"{gpu.load * 100:.2f}%"
        })
    return gpu_data

def get_memory_usage():
    """Get memory usage statistics."""
    memory_info = psutil.virtual_memory()
    return {
        "Total Memory": f"{memory_info.total / (1024 ** 3):.2f} GB",
        "Available Memory": f"{memory_info.available / (1024 ** 3):.2f} GB",
        "Used Memory": f"{memory_info.used / (1024 ** 3):.2f} GB",
        "Memory Usage": f"{memory_info.percent}%"
    }

def get_cpu_usage():
    """Get CPU usage statistics."""
    cpu_percent = psutil.cpu_percent(interval=1)
    return {"CPU Usage": f"{cpu_percent}%"}

def get_disk_usage(path=None):
    """Get disk usage statistics."""
    if path == None:
        path = input("please input the disk path(windows) like 'C:\\', if don't, will use root path on linux")
    if path == None:
        path = "/"
    disk_info = shutil.disk_usage(path)
    total = disk_info.total
    used = disk_info.used
    free = disk_info.free
    disk_usage_percent = (used / total) * 100
    return {
        "Total Disk Space": f"{total / (1024 ** 3):.2f} GB",
        "Used Disk Space": f"{used / (1024 ** 3):.2f} GB",
        "Free Disk Space": f"{free / (1024 ** 3):.2f} GB",
        "Disk Usage": f"{disk_usage_percent:.2f}%"
    }

def main():
    print("CPU Usage:")
    print(tabulate([get_cpu_usage().items()], headers=["Metric", "Value"], tablefmt="grid"))

    print("\nMemory Usage:")
    print(tabulate(get_memory_usage().items(), headers=["Metric", "Value"], tablefmt="grid"))

    print("\nGPU Usage:")
    print(tabulate(get_gpu_usage(), headers="keys", tablefmt="grid"))
