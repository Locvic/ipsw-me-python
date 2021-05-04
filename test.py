# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import ipsw_me # Import module

api = ipsw_me.API() # Initialize client

# Get device information by identifier
device = api.device_info("iPad4,7")
print(device.name) # iPad Mini 3 (WiFi)
print(device.boardconfig) # J85mAP
print(device.platform) # s5l8960x
print(device.boards) # {"boardconfig": "J85mAP", "platform": "s5l8960x", "cpid": 35168, "bdid": 50}
print(device.cpid) # 35168
print(device.bdid) # 50

# Get ipsw information by identifier and build id
ipsw = api.get_ipsw("iPad4,7", "15B150")
print(ipsw.version) # 11.1.1
print(ipsw.url) # appldnld.apple.com IPSW url
print(ipsw.buildid) # 15B150
print(ipsw.sha1sum, ipsw.md5sum, ipsw.filesize) # Return file information
print(ipsw.releasedate) # IPSW release date
print(ipsw.uploaddate) # IPSW upload date
print(ipsw.signed) # IPSW signed bool

model = api.get_model("A1670")
print(model)

devices = api.devices()
print(devices)

otas = api.get_ota_version("8.0")
for x in otas: print(x.url)

itunes = api.itunes("windows")
for x in itunes: print(x.x64biturl)

version_ipsw = api.version_ipsw("11.1")
print(version_ipsw)

get_ota_version = api.get_ota_version("11.2")
print(get_ota_version)

releases = api.releases()
print(releases)

get_device_keys = api.get_device_keys("iPhone7,1")
print(get_device_keys)