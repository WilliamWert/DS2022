#!/bin/bash

BUCKET_NAME=ds2022-dxg9tt
URL=https://www.ocregister.com/wp-content/uploads/2024/07/OCR-L-SURFSHOTOLYMPICS-0801-01-1.jpg?w=1024
FILE_NAME=olympic_surfing.jpg

# creating a bucket
aws s3 mb s3://$BUCKET_NAME

# grabbing image url
curl $URL > $FILE_NAME

# uploading the file to s3 bucket
aws s3 cp $FILE_NAME s3://$BUCKET_NAME/

# creating a url with a 7-day expiration

#temp_url=
aws s3 presign --expires-in 604800 s3://$BUCKET_NAME/$FILE_NAME
#echo $temp_url
