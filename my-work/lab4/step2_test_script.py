#!/usr/bin/python3

import boto3

# create client
s3 = boto3.client('s3', region_name="us-east-1")

# make request
response = s3.list_buckets()

# now iterate through the response:
for r in response['Buckets']:
  print(r['Name'])

bucket = 'ds2022-dxg9tt'
local_file = 'https://variety.com/wp-content/uploads/2022/12/MCDHANG_EC002.jpg'

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file,
    ACL = 'public-read'
)
