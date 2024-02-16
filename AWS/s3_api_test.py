import boto3
from botocore.exceptions import NoCredentialsError

AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
AWS_REGION = ''
bucket_name = 'server'
filename = 'test.jpg'


def list_s3_buckets():
    try:
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_KEY)

        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        print("S3 Buckets:")
        for bucket in buckets:
            print(f"- {bucket}")

    except NoCredentialsError:
        print("Credentials not available or incorrect.")


def upload_file(local_file_path, bucket_name, s3_file_name):
    try:
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_KEY)

        s3.upload_file(local_file_path, bucket_name, s3_file_name)
        print(f"File {s3_file_name} uploaded successfully.")

    except NoCredentialsError:
        print("Credentials not available or incorrect.")


def download_file(bucket_name, s3_file_name, local_file_path):
    try:
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_KEY)

        s3.download_file(bucket_name, s3_file_name, local_file_path)
        print(f"File {s3_file_name} downloaded successfully.")

    except NoCredentialsError:
        print("Credentials not available or incorrect.")


list_s3_buckets()
upload_file(filename, bucket_name, filename)
download_file(bucket_name, filename, filename)

# -------- Simple testing ---------
# Create an S3 client with the configured credentials
# s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY,
#                     aws_secret_access_key=AWS_SECRET_KEY)

# for bucket in s3.buckets.all():
#     print(bucket.name)

# # Upload a new file
# with open(filename, 'rb') as data:
#     s3.Bucket(bucket_name).put_object(Key='test.jpg', Body=data)


def create_s3_bucket(bucket_name, region='ap-southeast-2'):
    try:
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_KEY)
        location = {'LocationConstraint': region}
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration=location)
        # s3.create_bucket(Bucket=bucket_name)

        print(f'S3 bucket "{bucket_name}" created successfully.')

    except NoCredentialsError:
        print('AWS credentials not available.')
    except Exception as e:
        print(f'Error creating S3 bucket: {e}')


bucket_name = 'tdocexamplebucket1'
aws_region = 'ap-southeast-2'

create_s3_bucket(bucket_name, aws_region)

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY)

response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
