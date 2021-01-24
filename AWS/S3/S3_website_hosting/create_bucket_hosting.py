import boto3
import json


# enter bucket name
BUCKET_NAME = 'new-s3-bucket-spinningops'


def s3_client():
    s3 = boto3.client('s3')
    return s3


def create_bucket(bucket_name):
    """ creates a new s3 bucket """
    return s3_client().create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-central-1'
        }
    )


def create_bucket_policy():
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [
            {
                'Sid': 'PublicRead',
                'Effect': 'Allow',
                'Principal': '*',
                'Action': ['s3:*'],
                'Resource': f'arn:aws:s3:::{BUCKET_NAME}/*'
            }
        ]
    }
    
    # Convert the policy from JSON dict to string
    policy_string = json.dumps(bucket_policy)
    # Set the new policy
    return s3_client().put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=policy_string
    )


def enable_static_website_hosting():
    """ modify bucket for website hosting """

    website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
    }

    return s3_client().put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration=website_configuration
    )
    

if __name__ == '__main__':
    ''' execute the function you want,
    uncomment to reuse functions '''
    create_bucket(BUCKET_NAME)
    # host_static_website(WEBSITE_BUCKET_NAME)
    # create_bucket_policy()
    # enable_static_website_hosting()

