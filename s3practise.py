import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

buckets = response['Buckets']

for i in buckets:
    print(i['Name'])

#print(response)