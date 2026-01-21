import os
import getpass
from datetime import timedelta

username = getpass.getuser()

def find_playtime(world_name):
    if world_name == None:
        return ""
    
    total_time = timedelta(hours = 0, minutes = 0, seconds = 0)
    folder_path = rf"C:\Users\{username}\AppData\Roaming\Hytale\UserData\Saves\{world_name}\logs"
    logs = []
    has_hytale = "Hytale" in os.listdir(rf"C:\Users\{username}\AppData\Roaming")
    
    if has_hytale == False:
        return ""

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path) and filename[filename.index("."):len(filename)] == ".log":
            logs.append(filename)
    
    for i in range(len(logs)):
        with open(folder_path + "/" + logs[i]) as file:
            f = file.readline()[12:20]
            l = file.readlines()[-2][12:20]
            
            f_time = timedelta(hours = int(f[0:2]), minutes = int(f[3:5]), seconds = int(f[6:8]))
            l_time = timedelta(hours = int(l[0:2]), minutes = int(l[3:5]), seconds = int(l[6:8]))
            
            total_time += (l_time - f_time)
    
    if "," in str(total_time):
        return str(total_time)[8:15]
    else:
        return str(total_time)
    
find_playtime("Shlong")