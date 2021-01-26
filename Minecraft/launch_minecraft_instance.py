import boto3


client = boto3.client('ec2', region_name='eu-central-1')
ec2 = boto3.resource('ec2', region_name='eu-central-1')


def create_instance_minecraft():
    '''
        Create new instance with ami Minecraft.
    '''
    response = ec2.create_instances(
        ImageId='ami-05c01405261ec',
        InstanceType='c5.large',
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=['sg-0e32f0e14064'],
        KeyName='pemFile'
    )

    return response


def list_instances_id():
    '''
        List instances
    '''
    response = client.describe_instances()

    print('Instance ID: ')
    print(response['Reservations'][0]['Instances'][0]['InstanceId'])
    print('Instance State: ')
    return response['Reservations'][0]['Instances'][0]['Monitoring']


def delete_instance_minecraft():
    '''
        Delete instance Minecraft.
    '''
    response_instances = client.describe_instances()

    instance_id = response_instances['Reservations'][0]['Instances'][0]['InstanceId']

    response = client.terminate_instances(
    InstanceIds=[
        instance_id,
        ],
    )

    return response


# Uncomment the functions you need to use

# create_instance_minecraft()
list_instances_id()
# delete_instance_minecraft()


