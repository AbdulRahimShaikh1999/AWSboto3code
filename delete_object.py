import boto3
s3 = boto3.client("s3")



def delete_object(bucket, key):
    s3.delete_object(Bucket=bucket, Key=key)


delete_object("feedback-app-abdulrahimshaikh", "robots.txt")