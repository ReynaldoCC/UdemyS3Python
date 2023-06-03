import boto3

import utils

DEFAULT_BUCKET_NAME = 'testing-bucket-sss'

client = boto3.client('s3')

print('Bucket list: ')
utils.show_bucket_list(client=client)

# The bucket should be empty before try to delete it
client.delete_bucket(Bucket=DEFAULT_BUCKET_NAME)

print('Remaining bucket list: ')
utils.show_bucket_list(client=client)