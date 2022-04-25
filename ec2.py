import boto3

# def describeEc2Instance():
#     try:
#         ec2_resource=boto3.client("ec2")
#         print(ec2_resource.describe_instances())
#     except Exception as e:
#         print(e)

def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId="ami-04505e74c0741db8d",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro"
    )

    print(instances["Instances"][0]["InstanceId"])

# def get_public_ip(instance_id):
#     ec2_client = boto3.client("ec2", region_name="us-east-1")
#     reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")
#     li=[]
#     for reservation in reservations:
#         for instance in reservation['Instances']:
#             print(instance.get("PublicIpAddress"))
#             li.append(instance.get("PublicIpAddress"))
#     print(li)
#     return li

def get_running_instances():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")
    li=[]
    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
            newdict={}
            newdict["instance_id"]=instance_id
            newdict["instance_type"]=instance_type
            newdict["public_ip"]=public_ip
            li.append(newdict)
            print(f"{instance_id}, {instance_type}")
    
    return li


def stop_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)


def terminate_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)