import boto3

s3 = boto3.client('s3')

list_buckets = s3.list_buckets()

print("Buckets:")
for bucket in list_buckets['Buckets']:
    # print(f"  {bucket['Name']}")
    res = input(f"Do you want to delete the bucket '{bucket['Name']}'? (yes/no): ")
    if res.lower() == 'yes':
        try:

            # first, delete all objects in the bucket
            objects = s3.list_objects_v2(Bucket=bucket['Name'])
            if 'Contents' in objects:
                for obj in objects['Contents']:
                    s3.delete_object(Bucket=bucket['Name'], Key=obj['Key'])
                print(f"All objects in bucket '{bucket['Name']}' deleted successfully.")
            
            # also, disable versioning if it is enabled
            # versioning = s3.get_bucket_versioning(Bucket=bucket['Name'])    
            # if versioning.get('Status') == 'Enabled':
            #     s3.put_bucket_versioning(
            #         Bucket=bucket['Name'],
            #         VersioningConfiguration={'Status': 'Suspended'}
            #     )
            #     print(f"Versioning for bucket '{bucket['Name']}' has been suspended.")

            # now empty all the objects versions if versioning was enabled
            # if 'Versions' in objects:
            #     for version in objects['Versions']:
            #         s3.delete_object(
            #             Bucket=bucket['Name'],
            #             Key=version['Key'],
            #             VersionId=version['VersionId']
            #         )
            #     print(f"All versions in bucket '{bucket['Name']}' deleted successfully.")

            s3.delete_bucket(Bucket=bucket['Name'])
            print(f"Bucket '{bucket['Name']}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting bucket '{bucket['Name']}': {e}")
    else:
        print(f"Bucket '{bucket['Name']}' was not deleted.")