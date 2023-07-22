# aws_wrapper
creating a wrapper in Python that allow you to connect to AWS services using BOTO

in this project we connect AWS and Python using a library BOTO, documentation can be found here: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrations3.html

steps:
create an IAM user in AWS and add permissions for both S3 and EC2 and assign those permissions to the user.
Create access key for programmatic access for the user.
install AWS CLI
open VSC
do : aws configure (add both access and secret keys)
create an S3 bucket via console and keep it open for public access (NOTE: DO NOT store any personal data in it as its publically accessible)
copy the URI of the bucket
in vsc terminal: aws s3 ls 
 aws s3 cp <paste the uri> # means copy on our system in present location
 install boto 3 simply using: pip install boto3
 boto takes creds from aws cli

 create a new .py file and import boto and call the fucntion.
 create the file and add that file that you want to upload to s3
 check the bucket and the file should be uploaded.
