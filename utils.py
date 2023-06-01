import boto3


def show_bucket_list(client):
    response = client.list_buckets()
    if response.get('ResponseMetadata'):
        print(f'Response status: {response.get("ResponseMetadata").get("HTTPStatusCode")}')

        for bucket in response.get('Buckets'):
            print(f'Bucket Name: {bucket.get("Name")} created: {bucket.get("CreationDate")} ')
    else:
        print('Connection error')