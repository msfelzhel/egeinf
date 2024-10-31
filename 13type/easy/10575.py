from ipaddress import *


n = bin(118)[2:]
n1 = bin(193)[2:]
n2 = bin(24)[2:]
maskz = n.count('1') + n1.count('1') + n2.count('l')

for mask in range(33):
    net = ip_network(f'118.193.30.139/{mask}',0)
    print(net, net.netmask)
    
