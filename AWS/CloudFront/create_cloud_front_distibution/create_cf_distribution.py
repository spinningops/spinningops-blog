import boto3
from datetime import datetime



def cf_client():
    cf = boto3.client('cloudfront')
    return cf


def create_distribution_cf(bucket):
    CALLER_REFERENCE = 'my-references-{}'.format(datetime.now())
    DISTRIBUTION_ENABLED = True

    domain_name = bucket
    domain_of_site = domain_name
    domain_parser = '{}'.format(domain_of_site)

    bucket_name = bucket + '.s3.amazonaws.com'
    url_of_site = bucket_name
    url_parser = '{}'.format(url_of_site)

    S3 = 'S3-'

    

    response = cf_client().create_distribution(
        DistributionConfig=dict(
            CallerReference = CALLER_REFERENCE,
            DefaultRootObject = 'index.html',
            Origins = dict(
                Quantity = 1,
                Items = [
                    dict(
                        Id = S3+domain_parser,
                        DomainName = url_parser,
                        S3OriginConfig = dict(OriginAccessIdentity = '')
                    )
                ]
            ),
            DefaultCacheBehavior = dict(
                TargetOriginId = S3+domain_parser,
                ViewerProtocolPolicy = 'redirect-to-https',
                TrustedSigners = dict(Quantity=0, Enabled = False),
                ForwardedValues = dict(
                    Cookies = dict(Forward='all'),
                    Headers = dict(Quantity=0),
                    QueryString=False,
                    QueryStringCacheKeys = dict(Quantity=0)
                ),
                MinTTL = 1000
            ),
            Comment='Created from local script',
            Enabled=DISTRIBUTION_ENABLED
        )
    )
    return response


create_distribution_cf('spinningops.com')
