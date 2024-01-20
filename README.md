# Meraki Site Wide Controller
This PoV provides scripts for controlling various components of a Meraki site, such as networks, ssids, stp, traffic shaping, port configurations etc.

## Contacts
* Lakshya Tyagi

## Solution Components
* Cisco Meraki 
* Cisco Meraki Dashboard API

## Pre-Requisites

### Meraki API Key
In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:

Login to the Meraki dashboard
In the left-hand menu, navigate to Organization > Settings > Dashboard API access
Click on Enable access to the Cisco Meraki Dashboard API
Go to My Profile > API access
Under API access, click on Generate API key

Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. 


## Installation/Configuration

1. Clone/download this repository. 

2. Create a python virtual environment
```python
python3 -m venv <venv_name>
```

3. Activate python virtual environment and download dependencies.
```python
source <venv_name>/bin/activate

# Execute the following to download dependencies.
pip install -r requirements.txt
```

4. Add all required credentials in the .env file.
```python
# Meraki Credentials
MERAKI_BASE_URL = "https://api.meraki.com/api/v1"
MERAKI_API_KEY = ""
MERAKI_ORG_ID = ""
MERAKI_NETWORK_ID = ""
MERAKI_DEVICE_SERIAL = ""
```

## Usage

1. In the /configure_site directory, navigate to the directory which matches the task to carry out. Each directory has 2 scripts, a controller, a config. In the config script, add the required configuration by refering to the Meraki API docs.
2. Execute the following command
```python

python main.py -m <module_name>
```

3. The <module_name> will be one of the following:
```python
create_network
update_network
create_port_schedule
configure_rf_profile
list_snmp_settings
update_snmp_settings
create_ssids
update_stp
list_network_stacks
create_svi
list_syslog_servers
update_syslog_servers
list_traffic_shaping_settings
update_traffic_shaping_settings
get_traffic_analysis
```

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
