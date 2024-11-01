from ipaddress import * 

net = ip_network('0.0.0.0/255.255.128.0')
print(net)