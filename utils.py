import boto3


def show_bucket_list(client):
    response = client.list_buckets()
    if response.get('ResponseMetadata'):
        print(f'Response status: {response.get("ResponseMetadata").get("HTTPStatusCode")}')

        for bucket in response.get('Buckets'):
            print(f'Bucket Name: {bucket.get("Name")} created: {bucket.get("CreationDate")} ')
    else:
        print('Connection error')

def get_object_name_list(client, bucket_name):
    response = client.list_objects(Bucket=bucket_name)
    object_names = []
    for obj in response.get('Contents') or []:
        object_names.append(obj.get('Key'))
    return object_names

def show_objects_list_in_bucket(client, bucket_name):
    names = get_object_name_list(client, bucket_name)
    for name in names:
        print(name)
