import subprocess
import os
import datetime

# If enabled, the log file will be created in the current working folder.    
log_filename = "wifi_scanner.log"
FILE = os.path.join(os.getcwd(), log_filename)

# ct stores current time
ct = datetime.datetime.now()

scan_time = "WiFi scan started at: " + str(ct).split(".")[0]
print(scan_time)

#with open(FILE, "a") as file:
#    file.write("\n")
#    file.write("Scan Time:" + str(ct) + "\n")

def write_permission_check():
    try:
        with open(FILE, "a") as file:
            pass
    except OSError as error:
        print("Log file creation failed")
        sys.exit()
    finally:
        pass

#return all the available networks
networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

wifi_networks = networks.decode('ascii')

print(wifi_networks)

with open(FILE, "a") as file:
    file.write("\n")
    file.write(scan_time + "\n")
    file.write(wifi_networks + "\n")
