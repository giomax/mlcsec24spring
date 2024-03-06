import math
import ipaddress

#N1
print('giorgi')


#N2
a = 10
b = 5

addition_result = a + b
subtraction_result = a - b
multiplication_result = a * b
division_result = a / b

# Print the results
print("Addition:", addition_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)


#N3
try:
    radius = float(input("Enter Radius:"))
    area = math.pi * radius ** 2
    print("Your AREA IS : {}".format(area))
except:
    print(" ENTER FLOAT")


#N4
try:
    minute = float(input("Enter Minute:"))
    second = minute * 60
    print("Your Second IS : {}".format(second))
except:
    print("ENTER MINUTE")


#N5
host_address = ipaddress.IPv4Address('192.168.0.3')
network = ipaddress.IPv4Network(f'{host_address}/24', strict=False)
for ip in network:
    print(ip)
