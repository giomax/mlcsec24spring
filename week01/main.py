import math
import ipaddress


print('giorgi')

a = 5
b = 6
print(a+b)
try:
    radius = float(input("Enter Radius:"))
    area = math.pi * radius ** 2
    print("Your AREA IS : {}".format(area))
except:
    print(" ENTER FLOAT")


try:
    minute = float(input("Enter Minute:"))
    second = minute * 60
    print("Your Second IS : {}".format(second))
except:
    print("ENTER MINUTE")


host_address = ipaddress.IPv4Address('192.168.0.3')
network = ipaddress.IPv4Network(f'{host_address}/24', strict=False)
for ip in network:
    print(ip)
