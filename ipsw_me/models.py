# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from typing import Optional, Union
from datetime import datetime
from dateutil import tz

def convert_datetime(time: Optional[str]) -> datetime:
    if time is None: return time # early return
    obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    return obj.replace(tzinfo=tz.tzutc())

class Device:
    """
    Device object

    Available attributes:
    :name: - Device name
    :identifier: - Device identifier
    :boardconfig: - Device board configuration
    :platform: - Device platform
    :boards: - List of boards in dict form
    :cpid: - Device cpid
    :bdid: - Device bdid
    """

    def __init__(self, name: str, identifier: str, boardconfig: str, platform: str, firmwares: Optional[list], boards: Optional[list], cpid: int, bdid: int) -> None:
        self.name = name
        self.identifier = identifier
        self.boardconfig = boardconfig
        self.platform = platform
        self.firmwares = firmwares # list of dicts
        self.boards = boards # list of dicts
        self.cpid = cpid # int
        self.bdid = bdid # int
    
    def __repr__(self) -> str:
        return f'{self.name} [{self.identifier}]'

class IPSWFirmware:
    """
    IPSW Firmware object

    Available attributes:
    :identifier: - Device identifier
    :url: - IPSW url
    :version: - iOS version
    :buildid: - Build ID
    :sha1sum: - SHA1 Hash
    :md5sum: - MD5 Hash
    :sha256sum: - SHA256 Hash
    :filesize: - File size in bytes
    :releasedate: - Release date in datetime
    :uploaddate: - Upload date in datetime
    :signed: - IPSW signed bool
    """

    def __init__(self, identifier: str, url: str, version: str, buildid: str, sha1sum: str, md5sum: str, sha256sum: str, filesize: int, releasedate: Union[str, None], uploaddate: Union[str, None], signed: bool) -> None:
        self.identifier = identifier
        self.url = url
        self.version = version
        self.buildid = buildid
        self.sha1sum = sha1sum # hash
        self.md5sum = md5sum # hash
        self.sha256sum = sha256sum # hash
        self.filesize = filesize # in bytes
        self.releasedate = convert_datetime(releasedate) # datetime
        self.uploaddate = convert_datetime(uploaddate) # datetime
        self.signed = bool(signed) # signed bool

    def __repr__(self) -> str:
        return f'IPSW {self.identifier} {self.version} [{self.signed}]'

class iTunesFirmware:
    """
    iTunes Firmware object

    Available attributes:
    :platform: - Firmware platform
    :version: - Firmware version
    :datefound: - Firmware date found
    :url: - Firmware download url
    :x64biturl: - Firmware x64 download url
    :releasedate: - Firmware release date in datetime
    :uploaddate: - Firmware upload date in datetime
    """

    def __init__(self, platform: str, version: str, datefound: str, url: str, x64biturl: str, releasedate: str, uploaddate: str):
        self.platform = platform
        self.version = version
        self.datefound = convert_datetime(datefound)
        self.url = url
        self.x64biturl = x64biturl
        self.releasedate = convert_datetime(releasedate)
        self.uploaddate = convert_datetime(uploaddate)
    
    def __repr__(self) -> str:
        return f'iTunes {self.version} {self.platform}'

class DeviceKeys:
    """
    Device Keys object

    Available attributes:
    :identifier: - Device identifier
    :buildid: - Build ID
    :codename: - Codename
    :baseband: - Baseband
    :updateramdiskexists: - UpdateRamdiskExists bool
    :restoreramdiskexists: - RestoreRamdiskExists bool
    """

    def __init__(self, identifier: str, buildid: str, codename: str, baseband: str, updateramdiskexists: str, restoreramdiskexists: str):
        self.identifier = identifier
        self.buildid = buildid
        self.codename = codename
        self.baseband = baseband
        self.updateramdiskexists = updateramdiskexists
        self.restoreramdiskexists = restoreramdiskexists

class IPSWKeys:
    """
    IPSW Keys object

    Available attributes:
    :identifier: - Device identifier
    :buildid: - Build ID
    :codename: - Codename
    :updateramdiskexists: - UpdateRamdiskExists bool
    :restoreramdiskexists: - RestoreRamdiskExists bool
    :keys: - List of ipsw key
    """

    def __init__(self, identifier: str, buildid: str, codename: str, updateramdiskexists: str, restoreramdiskexists: str, keys: Optional[list]):
        self.identifier = identifier
        self.buildid = buildid
        self.codename = codename
        self.updateramdiskexists = updateramdiskexists
        self.restoreramdiskexists = restoreramdiskexists
        self.keys = keys

class KeyObject:
    """
    Key object

    Available attributes:
    :image: - Image name
    :filename: - Key filename
    :kbag: - Kbag
    :key: - Key
    :iv: - IV
    :date: - Date
    """

    def __init__(self, image: str, filename: str, kbag: str, key: str, iv: str, date: str):
        self.image = image
        self.filename = filename
        self.kbag = kbag
        self.key = key
        self.iv = iv
        self.date = convert_datetime(date)

class OTAFirmware:
    """
    OTA Firmware object

    Available attributes:
    :identifier: - Device identifier
    :buildid: - Build ID
    :version: - OTA version
    :url: - OTA download url
    :filesize: - File size in bytes
    :prerequisitebuildid: - Prerequisite build ID
    :prerequisiteversion: - Prerequisite version
    :releasetype: - Release type
    :uploaddate: - Upload date
    :releasedate: - Release date
    :marketingversion: - Marketing version
    :signed: - Signed bool
    """

    def __init__(self, identifier: str, buildid: str, version: str, url: str, filesize: int, prerequisitebuildid: str, prerequisiteversion: str, releasetype: str, uploaddate: str, releasedate: str, marketingversion: str, signed: bool):
        self.identifier = identifier
        self.buildid = buildid
        self.version = version
        self.url = url
        self.filesize = filesize
        self.prerequisitebuildid = prerequisitebuildid
        self.prerequisiteversion = prerequisiteversion
        self.releasetype = releasetype
        self.uploaddate = convert_datetime(uploaddate)
        self.releasedate = convert_datetime(releasedate)
        self.marketingversion = marketingversion
        self.signed = signed

class Release:
    def __init__(self, date: str, releases: Optional[list]):
        self.date = date
        self.releases = releases
