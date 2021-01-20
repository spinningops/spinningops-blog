import boto3
import pprint
from termcolor import colored


client = boto3.client('ce', region_name='us-east-1')


def costExplorerAmount():
    '''
        Get the current billing amount. 
    '''
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': '2021-01-01',
            'End': '2021-01-21'
        },
        Granularity='MONTHLY',
        Metrics=[
            'NetUnblendedCost',
        ]
    )

    pretty_dict_str = pprint.pformat(response['ResultsByTime'][0]['Total']['NetUnblendedCost']['Amount'])

    # This removes the ' at the start of the string amount and removes after the float .
    amount_output = pretty_dict_str[1:pretty_dict_str.index('.')]
    return 'The current billing amount is: $' + colored(amount_output, 'red')

    
print(costExplorerAmount())
