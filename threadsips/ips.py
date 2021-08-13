import ipaddress

ip_endereco = '192.168.0.1'
#ip_rede = '192.168.0.0/24'

#rede = ipaddress.ip_network(ip, strict=False)
endereco = ipaddress.ip_address(ip_endereco)

print(endereco + 100)

'''for ip in rede:
    print(ip)
'''