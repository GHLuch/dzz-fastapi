import boto3
s3 = boto3.client(
    service_name='s3',
    endpoint_url='https://s3.timeweb.cloud',
    aws_access_key_id="XROO37RWG03SKVMWYLO7", 
    aws_secret_access_key="EJ2VzFsEW0rDQv4VTWeKYfNHLHOLLz4tbpYNkhHo", 
    region_name="ru-1"
 )
