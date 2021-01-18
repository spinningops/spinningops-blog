import boto3
from datetime import datetime



def cf_client():
    cf = boto3.client('cloudfront')
    return cf


def get_cloudfront_distribution_id(bucket):

    bucket_origin = bucket + '.s3.amazonaws.com'
    cf_distro_id = None

    # Create a reusable Paginator
    paginator = cf_client().get_paginator('list_distributions')

    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate()

    for page in page_iterator:
        for distribution in page['DistributionList']['Items']:
            for cf_origin in distribution['Origins']['Items']:
                    if bucket_origin == cf_origin['DomainName']:
                            cf_distro_id = distribution['Id']
                            

    distID = cf_distro_id
    print(distID)
    return cf_distro_id


    """ cloudfront invalidation """
    cf_client().create_invalidation(
    DistributionId=distID,
    InvalidationBatch={
        'Paths': {
            'Quantity': 1,
            'Items': [
                '/*',
            ]
        },
        'CallerReference': 'my-references-{}'.format(datetime.now())
        }
    )
    
    return distID


# enter your domain name
url_of_site = 'spinningops.com'
url_parser = '{}'.format(url_of_site)
get_cloudfront_distribution_id(url_parser)