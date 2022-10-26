import boto3
client=boto3.client('s3')
list_bucket_Object=client.list_objects(Bucket='athiva-training',Delimiter='/',Prefix= 'VigneshNarayanan/Vignesh',)
print('list_bucket_Object\n',list_bucket_Object)
contents=list_bucket_Object['Contents']
for i in range(len(contents)):
    files=contents[i]['Key']
    print(files)
    print(type(files))
    response = client.put_object_tagging(
    Bucket='athiva-training',
    Key=files,
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


    get_tagging_status=client.get_object_tagging(
        Bucket='athiva-training',
        Key=files,)
    print('****get_tagging_status**** : \n',get_tagging_status)