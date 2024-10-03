#!/usr/bin/python3

import boto3
import requests

# create client
s3 = boto3.client('s3', region_name="us-east-1")

# Fetching and saving a file from the internet and uploading to S3

url = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGF5Y25vYWlyZ293YWJwYjB1azltamZ6cnFjdHoxZGZ4OXRwa3l0cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hzrvwvnbgIV6E/giphy.webp"

def upload_to_s3(url, bucket_name, s3_file_name):
    try:
        # Fetch the file content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for a failed request
        # Upload the file to S3
        s3.put_object(Bucket=bucket_name, Key=s3_file_name, Body=response.content, ACL = 'public-read')
        print(f"File uploaded successfully to s3://{bucket_name}/{s3_file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file from URL: {e}")
    except NoCredentialsError:
        print("Credentials not available for AWS S3")


bucket = 'ds2022-dxg9tt'
s3_file_name = 'dude_gif.gif'

upload_to_s3(url, bucket, s3_file_name)

# Presigning the file with a 7 day expiration and outputing presigned URL

bucket_name = 'ds2022-dxg9tt'
object_name = 'dude_gif'
expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )

print(response)
