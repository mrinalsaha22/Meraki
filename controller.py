"""
Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Lakshya Tyagi <ltyagi@cisco.com>"
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import os
import json
import requests
from dotenv import load_dotenv
from urllib.error import HTTPError


load_dotenv()

meraki_base_url = os.getenv("MERAKI_BASE_URL")
meraki_api_key = os.getenv("MERAKI_API_KEY")

#header
headers = {
    'X-Cisco-Meraki-API-Key': meraki_api_key,
    'Content-Type': 'application/json'
}


# List all organizations under an API key
def meraki_api_org_list():
    org_array = []
    
    try:
        response = requests.get(url = f"{meraki_base_url}/organizations", headers= headers)
        if response.status_code == 200:
            org_list = response.json()
            for org in org_list:
                #org_array.append(org_name["name"])
                org_dets = {}
                org_dets["org_id"] = org["id"]
                org_dets["org_name"] = org["name"]
                org_array.append(org_dets)
        else:
            print("Meraki API Org List. API Call Unsuccessful.")
    except HTTPError as http:
        print(http)
    except Exception as ex:
        print(ex)
    
    return org_array
            
#result = meraki_api_org_list()
#print(result)

# List all networks in an organization
def meraki_api_network_list(meraki_org_id):
    network_array = []
    
    try:
        response = requests.get(url = f"{meraki_base_url}/organizations/{meraki_org_id}/networks", headers= headers)
        if response.status_code == 200:
            network_list = response.json()
            #print(network_list)
            for network in network_list:
                network_dets = {}
                network_dets["network_id"] = network["id"]
                network_dets["name"] = network["name"]
                network_array.append(network_dets)
        else:
            print("meraki_api_network_list. API Call Unsuccessful.")
    except HTTPError as http:
        print(http)
    except Exception as ex:
        print(ex)
    
    return network_array

#result = meraki_api_network_list('965749')
#print(result)


# List all devices in a network
def meraki_api_list_network_device(meraki_network_id):
    device_array = []
    try:
        response = requests.get(url = f"{meraki_base_url}/networks/{meraki_network_id}/devices", headers= headers)
        if response.status_code == 200:
            device_list = response.json()
            for device in device_list:
                device_dets = {}
                device_dets["serial"] = device["serial"]
                device_dets["name"] = device["name"]
                device_array.append(device_dets)
        else:
            print("meraki_api_list_network_device. API Call Unsuccessful.")
    except HTTPError as http:
        print(http)
    except Exception as ex:
        print(ex)
    
    return device_array

#result = meraki_api_list_network_device('L_585467951558176886')
#print(result)

# Update device names based on serial ID
def meraki_api_update_network_device_name(meraki_device_serial, meraki_device_name):
    payload = json.dumps({
        "name": meraki_device_name,
        })
    try:
        response = requests.request("PUT", url = f"{meraki_base_url}/devices/{meraki_device_serial}", headers= headers, data=payload)
        if response.status_code == 200:
            res = response.json()
            print(f"Device name changed to {meraki_device_name}")
        else:
            print("meraki_api_update_network_device_name. API Call Unsuccessful.")
    except HTTPError as http:
        print(http)
    except Exception as ex:
        print(ex)
    
    return res

#result = meraki_api_update_network_device_name('Q2AP-NMHP-WJDM', "New Switch")
#print(result)



# Configure spanning tree /network level : DONE
# Setting timezone /network level
# Traffic analytics /network level : DONE
# Syslog servers /network level: DONE
# Maintenance Window for firmware updates
# SNMP access : DONE
# Add a network, Update a network: DONE
# Script to integrate with webhooks
# Traffic shaping for SSID: DONE 
# Define a RF profile, update a RF profile
# Choose bands per ssid
# Configure port schedule
