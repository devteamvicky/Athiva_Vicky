import boto3

s3_client = boto3.client("s3")
bucket_name = "athiva-training"
paginator = s3_client.get_paginator("list_objects_v2")
response = paginator.paginate(Bucket=bucket_name,
                            Delimiter='/',
                            Prefix='VigneshNarayanan/Paginator_5000_Files',
                            PaginationConfig={"PageSize": 2})
for page in response:
    files = page.get("Contents")
    for file in files:
        print(f"file_name: {file['Key']}, size: {file['Size']}")
        print("=" * 90)