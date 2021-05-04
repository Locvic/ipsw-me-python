# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import requests

from .models import Device, IPSWFirmware, iTunesFirmware, DeviceKeys, IPSWKeys, KeyObject, OTAFirmware, Release
from typing import Dict, List, Optional

class API(object):
    def __init__(self) -> None:
        """
        Setup object and define API endpoints
        """
        self.version = 'v4'
        self.base = f'https://api.ipsw.me/{self.version}'
    
    def __send_request(self, endpoint: str) -> Dict:
        with requests.get(self.base + endpoint) as req:
            if req.status_code == 200:
                return req.json()
            raise requests.HTTPError(req.status_code, self.base + endpoint)
    
    def device_info(self, identifier: str, type_query: Optional[str] = None) -> Device:
        """
        Endpoint: /device/:identifier
        Returns device information and firmwares

        :param type_query: specify firmware type (ota, ipsw)
        """
        endpoint = f'/device/{identifier}'
        if type_query: endpoint += f'?type={type_query}'
        data = self.__send_request(endpoint)
        data['firmwares'] = [IPSWFirmware(**firmware) for firmware in data['firmwares']]
        return Device(**data)
    
    def devices(self, keys_only: Optional[bool] = None) -> List:
        """
        Endpoint: /devices
        Returns a list of all devices known to IPSW Downloads

        :param keys_only: bool specified to only get devices with firmware keys
        """
        endpoint = f'/devices'
        if keys_only: endpoint += '?keysOnly=' + str(keys_only).lower()
        data = self.__send_request('/devices')
        devices = []
        for device in data:
            device['firmwares'] = []
            devices.append(Device(**device))
        return devices

    def get_ipsw(self, identifier: str, buildid: str) -> IPSWFirmware:
        """
        Endpoint: /ipsw/:identifier/:buildid
        Returns IPSW Firmware information for specified identifier & buildid

        :param identifier: device identifier
        :param buildid: build ID
        """
        data = self.__send_request(f'/ipsw/{identifier}/{buildid}')
        return IPSWFirmware(**data)
    
    def version_ipsw(self, version: str) -> List:
        """
        Endpoint: /ipsw/:version
        Returns list of IPSW Firmware information for a specific version

        :param version: version number
        """
        data = self.__send_request(f'/ipsw/{version}')
        return [IPSWFirmware(**firmware) for firmware in data]

    def itunes(self, platform: str) -> List:
        """
        Endpoint: /itunes/:platform
        Returns list of iTunesFirmware for specified platform

        :param platform: platform name (windows, macos)
        """
        data = self.__send_request(f'/itunes/{platform}')
        firmwares = []
        for firmware in data:
            firmware['x64biturl'] = firmware.pop('64biturl')
            firmwares.append(iTunesFirmware(**firmware))
        return firmwares
    
    def get_device_keys(self, identifier: str) -> DeviceKeys:
        """
        Endpoint: /keys/device/:identifier
        Returns list of DeviceKeys objects for specified device identifier

        :param identifier: device identifier 
        """
        data = self.__send_request(f'/keys/device/{identifier}')
        return [DeviceKeys(**x) for x in data]
    
    def get_ipsw_keys(self, identifier: str, buildid: str) -> IPSWKeys:
        """
        Endpoint: /keys/ipsw/:identifier/:buildid
        Returns list of IPSWKeys objects for specified identifier and build ID

        :param identifier: device identifier 
        :param buildid: device build ID 
        """
        data = self.__send_request(f'/keys/ipsw/{identifier}/{buildid}')
        data['keys'] = [KeyObject(**key) for key in data['keys']]
        return IPSWKeys(**data)
    
    def get_model(self, model: str) -> str:
        """
        Endpoint: /model/:model
        Returns the device identifier from the :model: parameter

        :param model: device model
        """
        data = self.__send_request(f'/model/{model}')
        return data['identifier']
    
    def get_ota(self, identifier: str, buildid: str) -> OTAFirmware:
        """
        Endpoint: /ota/:identifier/:buildid
        Returns OTA information for specified device identifier and build ID

        :param identifier: device identifier
        :param buildid: build ID
        """
        data = self.__send_request(f'/ota/{identifier}/{buildid}')
        return OTAFirmware(**data)
    
    def get_ota_version(self, version: str) -> List:
        """
        Endpoint: /ota/:version
        Return list of OTA information for specified version

        :param version: OTA version
        """
        data = self.__send_request(f'/ota/{version}')
        return [OTAFirmware(**ota) for ota in data]
    
    def releases(self) -> List:
        """
        Endpoint: /releases
        Returns list of releases
        """
        data = self.__send_request('/releases')
        return [Release(**release) for release in data]