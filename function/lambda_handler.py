
import socket, boto3

ec2 = boto3.client('ec2', region_name='us-east-1')   

def scan(port, server_ip='127.0.0.1'):
    soc = socket.socket()
    try:
        soc.connect((server_ip)) #testing port connectivity 
        return True 
    except: 
        return False 
    finally: 
        soc.close()

def beginPortScan(server_ip):
    no_connection = []
    connection = []
    for port in list(range(0,1024)):
        if server_ip != None:
            if scan(port, server_ip):
                print(f"{server_ip} CONNECTED to port {port}")
                connection.append(server_ip)
            else:
                # print(f"Unable to connnect to {server_ip}:{port}")
                no_connection.append(server_ip)
    print(f"Server: {server_ip} Open: {len(connection)} Closed: {len(no_connection)}")
                

def init():
    data = ec2.describe_instances()
    data.get('Reservations')[0].get('Instances')[0].get('PublicIpAddress')
    for i,d in enumerate(data.get('Reservations')):
        ip = d.get('Instances')[0].get('PublicIpAddress')
        if ip != 'None':
             beginPortScan(ip)

def lambda_handler(event, context):
    init()

    
