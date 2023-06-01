import boto3
import os


DEFAULT_BUCKET_NAME = 'testing-bucket-sss'
subfolder_name_first_level = 'samples/'
subfolder_name_second_level = os.path.join(subfolder_name_first_level, 'exercice/')

client = boto3.client('s3')

# difference between name of folder or file objects is the '/' character in the end of the name,
# folder have the slash '/' and file not.
client.put_object(Bucket=DEFAULT_BUCKET_NAME, Key=subfolder_name_first_level)
client.put_object(Bucket=DEFAULT_BUCKET_NAME, Key=subfolder_name_second_level)
