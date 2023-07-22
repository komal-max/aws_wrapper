def my_buckets(my_s3_obj):
    for bucket in my_s3_obj.buckets.all():
        print(bucket.name)

def upload_file(my_s3_obj,bucket_name,file_path,key_name):
    file_contents=open(file_path,'rb') #now we have a binary data in file_contents
    my_s3_obj.Bucket(bucket_name).put_object(Key=key_name,Body=file_contents) #check boto3 doc for uploading a new file
    file_contents.close() #close the file
    print("file has been uploaded successfully!")

def list_files(my_s3_obj,bucket_name):
    print(f"Files in {bucket_name} are: " )
    for object in my_s3_obj.Bucket(bucket_name).objects.all():
        print(object.key)

# for creating an s3 bucket:

def create_s3_bucket(my_s3_obj,bucket_name):
    my_s3_obj.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={
    'LocationConstraint': 'ap-southeast-2'})  # gives incompatible location constraint error, can try other regions as well
    print(f"bucket {bucket_name} created successfully!")
