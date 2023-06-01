import boto3


client =  boto3.client('s3')

response = client.list_buckets()

if response.get('ResponseMetadata'):
    print(f'Response status: {response.get("ResponseMetadata").get("HTTPStatusCode")}')

    for bucket in response.get('Buckets'):
        print(f'Bucket Name: {bucket.get("Name")} created: {bucket.get("CreationDate")} ')
