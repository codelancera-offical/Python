import GPUtil
import psutil
import shutil
import os
import sys
import subprocess
from tabulate import tabulate

# computer status tools
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

def get_disk_usage():
    """Get disk usage statistics for all mounted disks."""
    disk_partitions = psutil.disk_partitions()
    disk_data = []
    for partition in disk_partitions:
        path = partition.mountpoint
        try:
            disk_info = shutil.disk_usage(path)
            total = disk_info.total
            used = disk_info.used
            free = disk_info.free
            disk_usage_percent = (used / total) * 100
            disk_data.append({
                "Disk": path,
                "Total Disk Space": f"{total / (1024 ** 3):.2f} GB",
                "Used Disk Space": f"{used / (1024 ** 3):.2f} GB",
                "Free Disk Space": f"{free / (1024 ** 3):.2f} GB",
                "Disk Usage": f"{disk_usage_percent:.2f}%"
            })
        except PermissionError:
            # Skipping disks that cannot be accessed
            continue
    return disk_data

def get_computer_status():
     # CPU usage
    print("CPU Usage:")
    cpu_data = get_cpu_usage()
    print(tabulate([cpu_data], headers="keys", tablefmt="grid"))
    print()  # 空行用于分隔

    # Memory usage
    print("Memory Usage:")
    memory_data = get_memory_usage()
    print(tabulate([memory_data], headers="keys", tablefmt="grid"))
    print()  # 空行用于分隔

    # Disk usage for all disks
    print("Disk Usage:")
    disk_data = get_disk_usage()
    for disk in disk_data:
        print(tabulate([disk], headers="keys", tablefmt="grid"))
        print()  # 每个磁盘的信息后添加空行用于分隔

    # GPU usage
    print("GPU Usage:")
    gpu_data = get_gpu_usage()
    print(tabulate(gpu_data, headers="keys", tablefmt="grid"))  # 由于可能有多个GPU，所以这里直接打印所有GPU的信息

# env path tools
def show_env_var(env_var_name=None):
    if env_var_name != None:
        value= os.environ.get(env_var_name)
        if value:
            print(f"{env_var_name}={value}")
        else:
            print(f"环境变量 '{env_var_name}' 不存在")
    else:
        print(f"----------OS env variables----------")
        # 计算最长的环境变量名的长度
        max_len = max(len(key) for key in os.environ.keys())
        
        # 打印每个环境变量，使用动态宽度对齐等号
        for key, value in os.environ.items():
            print(f"{key.ljust(max_len)} = {value}")

def add_env_var(env_var_name, env_var_value, user_scope=True):
    scope_flag = '/M' if not user_scope else ''

    try:
        command = f'setx {env_var_name} "{env_var_value}" {scope_flag}'

        subprocess.run(command, shell=True, check=True)
        print(f"env var '{env_var_name}' added successfully, value: {env_var_value}")
        
    except subprocess.CalledProcessError as e:
        print(f"error: {e}")

        
def main():
    pass
if __name__ == "__main__":
    main()

