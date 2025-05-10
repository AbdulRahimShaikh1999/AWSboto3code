import boto3 

s3 = boto3.client('s3')



url = s3.generate_presigned_url('get_object',Params={'Bucket': "my-cicd-demo-site-abdul-rahim-shaikh", 'Key': "robots.txt"}, ExpiresIn=60)

print(url)