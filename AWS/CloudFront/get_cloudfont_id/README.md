# CloudFront list distribution ID

### Create env
Install virtualenv  
`sudo apt install python3-pip`  
`sudo apt-get install python3-virtualenv`  

This version 20.0.23 works with ubuntu 20.04  
`pip3 install virtualenv==20.0.23`  

Create virtualenv  
`virtualenv .venv`  

Activate the env  
`source .venv/bin/activate`  

### Get / List cloudFront distribution ID
Install boto3  
`pip3 install boto3`  

Run the script  
`get_cf_distribution_id.py`  

