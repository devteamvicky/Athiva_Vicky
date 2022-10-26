import boto3
client=boto3.client('s3')
list_bucket_Object=client.list_objects(Bucket='athiva-training')
print('List Of Object : \n',list_bucket_Object)
response = client.put_object_tagging(
    Bucket='athiva-training',
    Key='VigneshNarayanan/Vignesh\\file_2.txt',
    Tagging={
            'TagSet': [
                {
                    'Key':'owner',
                    'Value':'VigneshNarayanan',
                },
                {
                    'Key': 'Task',
                    'Value': 's3-training',
                },
            ]
        })
print('tagging response',response)
get_tagging_status = client.get_object_tagging(
    Bucket='athiva-training',
    Key='VigneshNarayanan/Vignesh\\file_2.txt')
print('****get_tagging_status**** : \n', get_tagging_status)