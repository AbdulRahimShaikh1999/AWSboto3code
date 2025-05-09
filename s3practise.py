import boto3

s3 = boto3.client('s3')

s3.create_bucket(Bucket='testingabucketnow2025')

s3.upload_file(file_path='C:/Users/abdul/Downloads/boto3_practise/test_textfile.txt', bucket_name='testingabucketnow2025', object_key='abdulsfile', ContentType='text/plain')