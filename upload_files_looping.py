import json
import json
import boto3
import glob
# s3 = boto3.resource('s3')

client=boto3.client('s3')

def multiple_uploadfile(source,bucketname,destination=None):
    if destination is None:
        destination=source
    response=client.upload_file(source,bucketname,destination)
    print("successfully uploded",response)

files=glob.glob("saravanansir_5_files/*")
for i in files:
    print(i)
#using for loop for iterate every files and upload
for i in files:
    view_file=multiple_uploadfile(i,'athiva-training','Vignesh/looptask/')
    print(view_file)
response=client.list_buckets()
print(response)
botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the ListBuckets operation: Access Denied
response=client.list_objects(Bucket='athiva-training')
print(response)
'''{'ResponseMetadata': 'u'}'''