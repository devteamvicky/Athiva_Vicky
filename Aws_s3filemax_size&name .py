
import boto3

client = boto3.client('s3')
response = client.list_objects(Bucket='athiva-training')
print(response)
lenth = len(response['Contents'])
print(lenth)
contents = response['Contents']
print('contents \n',contents)

array=[]
dic={}

for i in range(len(contents)):
    key = contents[i]['Key']
    size=contents[i]['Size']
    dic[key]=size
    array.append(size)
print('FileSize: \n',array)
print('dictionery: \n ',dic)
print('length :\n ',len(dic))


largest=array[0]
for i in array:
    if i > largest:
        largest=i
maxmimu=largest


dictvicky={}
lis=[]
for key, value in dic.items():
    if value == maxmimu:
        # lis.append(key)
        # lis.append(value)
        dictvicky['FileName']=key
        dictvicky['Size']=value
        lis.append(dictvicky.copy())
print('The Maximum FileSize in S3-Athivan-Training Bucket: \n',lis)

Smallest=array[0]
for i in array:
    if i <= Smallest:
        Smallest=i
minima=Smallest

dictvicky1={}
lis1=[]

for key, value in dic.items():
    if value == minima:
        # lis.append(key)
        # lis.append(value)
        dictvicky1['FileName']=key
        dictvicky1['Size']=value
        lis1.append(dictvicky1.copy())
print('The Minimum FileSize in S3-Athivan-Training Bucket: \n',lis1)






''' i want my Result output my imagination 
lowest file {filename,size},
            {filename,size},
            {filename,size},
            {filename,size}
largest file {filename,size}
'''


