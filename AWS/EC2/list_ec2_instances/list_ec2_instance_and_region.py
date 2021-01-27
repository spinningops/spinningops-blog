import boto3


client = boto3.client('ec2')
client_region = boto3.client('ec2', region_name='us-east-1')



def list_aws_regions():
    '''
        List all AWS regions
    '''
    client = boto3.client('ec2')
    regions = client.describe_regions()['Regions']
    for region in regions:
        region_name=region['RegionName']
        print(region_name)


def list_instances_id():
    '''
        List instances in a specific region.
        to list instances in other region change the parameter region_name in client_region variable.
    '''
    response = client_region.describe_instances()

    try:
        print('Instance ID: ')
        print(response['Reservations'][0]['Instances'][0]['InstanceId'])
        print('Instance IP: ')
        print(response['Reservations'][0]['Instances'][0]['PublicIpAddress'])
        print('Instance State: ')
    except:
        pass
    return response['Reservations'][0]['Instances'][0]['Monitoring']


def delete_instances_by_id():
    '''
        Delete instances by ID.
        make sure to use the region your instances are located.
    '''
    response = client_region.terminate_instances(
    InstanceIds=[
        'i-00371c89d19596cdf',
        ],
    )

    return response


# uncomment the function you want to use 

# list_aws_regions()
# list_instances_id()
delete_instances_by_id()

