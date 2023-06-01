import os
import boto3
import uuid


DEFAULT_BUCKET_NAME = 'testing-bucket-sss'
current_path = os.getcwd()
data_folder = os.path.join(current_path, 'data')

client = boto3.client('s3')

for root, dir, files in os.walk(data_folder, topdown=False):
    for file in files:
        uploaded_name = f'{uuid.uuid4()}.csv'
        file_path = os.path.join(data_folder, file) 
        print(f'Uploading file {file_path}, with name {uploaded_name} to Bucket {DEFAULT_BUCKET_NAME} ...')
        client.upload_file(file_path, DEFAULT_BUCKET_NAME, uploaded_name)
        print('File uploaded')
