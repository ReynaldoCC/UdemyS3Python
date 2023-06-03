import boto3

import utils

NEW_BUCKET_NAME = 'testing-bucket-sss'

client = boto3.client('s3')

utils.show_bucket_list(client=client)

client.create_bucket(Bucket=NEW_BUCKET_NAME)

utils.show_bucket_list(client=client)
