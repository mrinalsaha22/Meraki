""" Copyright (c) 2020 Cisco and/or its affiliates.
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

import os
from argparse import ArgumentParser
import urllib3
from configure_site.network import configure_networks
from configure_site.port_schedule import configure_port_schedule
from configure_site.rf_profile import rfprofile_configuration
from configure_site.snmp import update_snmp
from configure_site.ssid import create_ssids
from configure_site.stp import update_stp
from configure_site.svi import create_meraki_svi
from configure_site.syslog_servers import configure_syslog_servers
#from configure_site.traffic_shaping import configure_traffic_shaping
from monitor.traffic_analytics import traffic_analytics
import logging

urllib3.disable_warnings()

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


if __name__=='__main__':
    #Argument Parser
    argparser=ArgumentParser()
    argparser.add_argument('-m', '--modules', required=False)
    args=argparser.parse_args()

    print('Starting Backup Workflow')

    try:
        if args.modules:
            if args.modules == 'create_network':
                logging.info("Creating a network.")
                configure_networks.create_network()
            elif args.modules == 'update_network':
                logging.info("Updating network.")
                configure_networks.update_network()
            elif args.modules == 'create_port_schedule':
                logging.info("Creating port schedule.")
                configure_port_schedule.create_port_schedule()
            elif args.modules == 'configure_rf_profile':
                logging.info("Configuring RF Profile")
                rfprofile_configuration.configure_rf_profile()
            elif args.modules == 'list_snmp_settings':
                logging.info("Listing SNMP Settings")
                update_snmp.list_snmp_settings()
            elif args.modules == 'update_snmp_settings':
                logging.info("Updating SNMP Settings.")
                update_snmp.update_snmp_settings()
            elif args.modules == 'create_ssids':
                logging.info("Creating SSID.")
                create_ssids.createSSIDs()
            elif args.modules == 'update_stp':
                logging.info("Updating STP Configurations.")
                update_stp.update_stp()
            elif args.modules == 'list_network_stacks':
                logging.info("Listing Network Switch Stacks.")
                create_meraki_svi.list_network_stacks()
            elif args.modules == 'create_svi':
                logging.info("Creating SVI")
                create_meraki_svi.create_svi()
            elif args.modules == 'list_syslog_servers':
                logging.info("Listing all syslog servers.")
                configure_syslog_servers.list_syslog_servers()
            elif args.modules == 'update_syslog_servers':
                configure_syslog_servers.update_syslog_servers()
            elif args.modules == 'list_traffic_shaping_settings':
                logging.info("Listing Traffic Shaping Settings.")
                configure_traffic_shaping.list_traffic_shaping()
            elif args.modules == 'update_traffic_shaping_settings':
                logging.info("Updating Traffic Settings.")
                configure_traffic_shaping.update_traffic_shaping_settings()
            elif args.modules == 'get_traffic_analytics':
                logging.info("Getting Traffic Analysis.")
                traffic_analytics.get_traffic_analytics()
            else:
                logging.info("Please select a correct module.")

    except Exception as error:
        logging.info(error)
    finally:
        logging.info('Action Completed')
