import pandas as pd
import random

def generate_network_data(num_samples):
    data = []
    common_ports = {  # Dictionary of common ports
        80: "HTTP",
        443: "HTTPS",
        22: "SSH",
        25: "SMTP",
        53: "DNS"
    }
    for _ in range(num_samples):
        packet_size = random.randint(50, 1500)  # Packet size
        payload = random.randint(0,1024) #payload size
        request_duration = random.randint(1, 100)  #Random Duration
        destination_port = random.choice(list(common_ports.keys()))
        data.append([packet_size, payload, request_duration,destination_port])
    return data

network_data = generate_network_data(200)

df = pd.DataFrame(network_data)#columns=['Packet_Size', 'Payload', 'Request Duration', 'Destionation Port']
df.to_csv('network_data.csv', index=False, header=False)