import boto3

from aws_wrapper import my_buckets,upload_file,list_files,create_s3_bucket

my_s3_obj = boto3.resource('s3') #boto will add all s3 fns in obj_name for this script

# print (dir(obj_name))  #to see list sll of s3 operations 

file_path='test.txt'

my_buckets(my_s3_obj)

upload_file(my_s3_obj,'mypython-project-bucket',file_path,'test.txt')

list_files(my_s3_obj,'mypython-project-bucket')

create_s3_bucket(my_s3_obj,'new-bucket')