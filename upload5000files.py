import glob
import os
import boto3
client=boto3.client('s3')
files=glob.glob('files/*')
file=files[0]
# print(file)
filenamae=os.path.basename(file)
print(filenamae)
start=0
count=1
for i in range(1,5001):
    print(i)
    start=start+1
    # print(type(start))
    type_casting=str(start)
    # print(type_casting)
    # print(type(type_casting))
#     print(type(i))
#     print(i)
    file_name=filenamae+type_casting
    # print(type(file_name))
    response=client.upload_file(file,"athiva-training","VigneshNarayanan/Paginator_5000_Files"+file_name)
    print(count,response)
    count += 1

