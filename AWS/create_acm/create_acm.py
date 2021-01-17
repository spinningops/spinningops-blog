import boto3


# enter domain name
DOMAIN_NAME = 'spinningops.com'


def create_acm(bucket):
    acm = boto3.client('acm')

    domain_name = bucket
    domain_of_site = domain_name
    domain_parser = '{}'.format(domain_of_site)

    """ request ACM certificate """
    acm.request_certificate(
        DomainName=domain_parser,
        ValidationMethod='DNS',
        
        
        DomainValidationOptions=[
            {
                'DomainName': domain_parser,
                'ValidationDomain': domain_parser
            },
        ],
    )

    return acm


def list_acm_certs(bucket):
    acm = boto3.client('acm')
    # List certificates with the pagination interface and sort domain
    website_name = bucket
    cert_arn_id = None

    paginator = acm.get_paginator('list_certificates')
    for response in paginator.paginate():
        for certificate in response['CertificateSummaryList']:
            # to print all your certificates in your account uncomment the next line
            # print("Certificate found {}".format(certificate['DomainName']))
            if website_name == certificate['DomainName']:
                cert_arn_id = certificate['CertificateArn']
                print("The Certificate arn ID for {} is:\n {}".format(website_name, cert_arn_id))

                return cert_arn_id


if __name__ == '__main__':
    ''' execute the function you want,
    uncomment to reuse functions '''
    # create_acm(DOMAIN_NAME)
    list_acm_certs(DOMAIN_NAME)