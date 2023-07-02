import re
import datetime

log_path="setupapi.dev2.log"
usb_devices={
    "device_vendor_id":[],
    "device_product_id":[],
    "device_instance_id":[],
    "event_time":[],
}
usb_regex=r'^>>>  \[Device Install.*#(Disk&Ven_[A-Za-z0-9]+)&(Prod_([\w\s\S]+?))&(Rev_([\w\s\S]+?))#([\w\s\S]+?)#.*\]'
# Read the contents of the setupapi.dev.log file
with open(log_path, "r") as log_file:
     # Store information about each USB device in a dictionary
     for line in log_file:
        # Find all USB device installation events and extract information about each device
        match=re.search(usb_regex, line)
        if(match!=None):
            event_time=next(log_file).split("start ")[1].strip()
            #print(match.groups())
            usb_devices["device_vendor_id"].append(match.groups()[0])
            usb_devices["device_product_id"].append(match.groups()[1])
            usb_devices["device_instance_id"].append(match.groups()[2])
            usb_devices["event_time"].append(event_time)

print(usb_devices)