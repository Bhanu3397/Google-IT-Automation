import shutil
import psutil
from networks import *
#check disk usage function to check if it's free more than 20%
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage ("/") or not check_cpu_usage(): #returning if either of two is false
    print("Error")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")