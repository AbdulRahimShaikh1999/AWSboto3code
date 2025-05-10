import boto3


s3 = boto3.client("s3")

s3.put_object_acl(Bucket='feedback-app-abdulrahimshaikh',
    Key='favicon.ico',
    ACL='public_read' )