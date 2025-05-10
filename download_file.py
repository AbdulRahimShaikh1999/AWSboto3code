import boto3
s3 = boto3.client("s3")

s3.download_file("feedback-app-abdulrahimshaikh", "index.html", "C:/Users/abdul/Downloads/boto3_practise/newfile.txt")