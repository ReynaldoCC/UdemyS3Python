import os
import boto3


DEFAULT_BUCKET_NAME = 'testing-bucket-sss'
current_path = os.getcwd()
downloads_path = os.path.join(current_path, 'downloads')

client =  boto3.client('s3')


def download_files(file_name, new_file_name=None):

    downlaoded_file_name = os.path.join(downloads_path, 
                                        new_file_name if new_file_name else file_name)
    client.download_file(Bucket=DEFAULT_BUCKET_NAME,
                         Key=file_name,
                         Filename=downlaoded_file_name)

response = client.list_objects(Bucket=DEFAULT_BUCKET_NAME)

for obj in response.get('Contents'):
    if obj.get('Size') and obj.get('Size') > 0:
        print(f'Downloading file {obj.get("Key")}....')
        if '/' in obj.get('Key'):
            new_name = obj.get('Key').split('/')[-1]
            download_files(obj.get('Key'), new_name)
        else:
            download_files(obj.get('Key'))
        print('Downloaded')
