Aws webpage with EC2 , S3 , IAM basic operations
##  NOTE  Don't delete instance with public IP 3.84.118.90 and instance id i-042dc4c244c1afe25	
For EC2
## Don't delete khawslabuser05@nuvelabs.com this user ##
Our application has both frontend and backend 

#URL link 
-- EC2 instance 
    -- http://3.84.118.90:5000/
-- Github link
    -- https://github.com/AkashInnovaccer/AwsClone
-- Dockerhub Repository link
    -- https://hub.docker.com/repository/docker/akash1308199/basicflask
    -- v3 is the newest version of the image

Routes for EC2

-   /ec2/create (will create ec2 instance)
-   /ec2/terminate (will get you to form where you can enter instance id and on submit this will delete instance)
-   /ec2/stop (will get you to form where you can enter instance id and on submit it will stop instance)
-   /ec2/list (will give you list of all running instances)

Routes for S3   ( This is not working in EC2 instance(HOSTED LINK) but working fine locally )

-   /s3/create (will create s3 bucket after the form)
-   /s3/list (will give list of all the buckets)
-   /s3/delete (will get you to form where you can enter instance id and on submit this will delete bucket)

Routes for IAM

-   /iam/create (will create s3 iam user after the form)
-   /iam/list (will give list of all the buckets)
-   /iam/delete (will get you to form where you can enter instance id and on submit this will delete iam user)

