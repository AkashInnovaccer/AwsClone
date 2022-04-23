import boto3

s3 = boto3.resource('s3')

def listbuckets():
    li=[]
    for bucket in s3.buckets.all():
        li.append(bucket.name)
        print(bucket.name)
    return li


def deletebuckets(name):
    bucket = s3.Bucket(name)
    bucket.delete()

def createbucket(name):
    s3.create_bucket(Bucket=name)

