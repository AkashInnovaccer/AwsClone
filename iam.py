import boto3

# IAM Services

# Create an IAM user by using create_user() function

def create_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=username)
    print(response)            

# list all the users Of IAM by using list_users() function

def list_users():
    iam = boto3.client("iam")
    paginator = iam.get_paginator('list_users')
    list2=[]
    for response in paginator.paginate():
        for user in response["Users"]:
            list2.append(user['UserName'])
            print(f"Username: {user['UserName']}, Arn: {user['Arn']}")   
    return list2                 

# Delete an IAM user by using delete_user() function

def delete_user(username):
    # Create IAM client
    iam = boto3.client('iam')

    # Delete a user
    response = iam.delete_user(
        UserName=username
    )
    print(response)

