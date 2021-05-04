# ipsw-me-python
<a href="https://github.com/Vislate/ipsw-me-python/blob/main/LICENSE">
<img src="https://img.shields.io/github/license/Vislate/ipsw-me-python?style=for-the-badge">
</a>
<a href="https://pypi.org/project/ipsw-me/">
<img src="https://img.shields.io/static/v1?label=pypi&message=ipsw-me&color=blue&style=for-the-badge">
</a>
<a href="#">
<img src="https://img.shields.io/github/downloads/Vislate/ipsw-me-python/total?style=for-the-badge">
</a>

Simple & lightweight IPSW.me API wrapper written in Python

Better docmentation coming soon [wiki](https://github.com/Vislate/ipsw-me-python/wiki)

# Installation
`pip install ipsw-me`

# Examples
```py
import ipsw_me # Import module

api = ipsw_me.API() # Initialize api

# Get device information by identifier
device = api.device_info("iPad4,7")
print(device.name) # iPad Mini 3 (WiFi)
print(device.boardconfig) # J85mAP
print(device.boards) # List of boards: [{"boardconfig": "J85mAP", "platform": "s5l8960x", "cpid": 35168, "bdid": 50}]

# Get ipsw information by identifier and build id
ipsw = api.get_ipsw("iPad4,7", "15B150")
print(ipsw.version) # 11.1.1
print(ipsw.url) # IPSW download url
print(ipsw.signed) # True or False
```

# Credits
[fxrcha](https://github.com/fxrcha) PyApple package

[IPSW.me](https://ipswdownloads.docs.apiary.io/) IPSW.me API documentation

[The iPhone Wiki](https://www.theiphonewiki.com/wiki/Main_Page) Device information and documentation
