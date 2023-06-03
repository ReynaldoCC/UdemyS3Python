import boto3

import utils


DEFAULT_BUCKET_NAME = 'testing-bucket-sss'

c = 0

client = boto3.client('s3')


print(f'List of objects in {DEFAULT_BUCKET_NAME}:')
utils.show_objects_list_in_bucket(client=client, bucket_name=DEFAULT_BUCKET_NAME)

# To effectivelly remove a folder in s3 the floder should be empty or we need to remove all the elelments inside the folder
# otherwise the folder still being in the bucket
print('Deletion process start')
for object_name in utils.get_object_name_list(client=client, 
                                              bucket_name=DEFAULT_BUCKET_NAME):
    if '/' in object_name:
        print(f'Deleting object {object_name}')
        client.delete_object(Bucket=DEFAULT_BUCKET_NAME, Key=object_name)
        c += 1
print('Deletion prossess finished')
print(f'{c} objects deleted')

print(f'List of objects in {DEFAULT_BUCKET_NAME}:')
utils.show_objects_list_in_bucket(client=client, bucket_name=DEFAULT_BUCKET_NAME)
