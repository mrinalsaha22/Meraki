import ipaddress


def convert_ip_to_subnet(ip, subnet_mask):
    subnet = ipaddress.ip_network(f"{ip}/{subnet_mask}",strict=False)
    return str(subnet)




# Campus ID, School ID, Switch Numbers.
SchID = ""
CamID = ""
SWnum = ""

# Network environment variables
net1020 = "10.125.224"
net30 = "10.125.225"
net40 = "10.125.226"
net50 = "10.125.227"
net70 = "10.125.229"
net105 = "10.125.230"


