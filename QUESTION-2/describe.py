
#All the information
'''import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
     print(Myec2)'''
 
#Instances information
import boto3

client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
    print(pythonins)
