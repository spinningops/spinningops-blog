# S3 Website Hosting

### create env
install virtualenv  
`sudo apt install python3-pip`  
`sudo apt-get install python3-virtualenv`  

this version 20.0.23 works with ubuntu 20.04  
`pip3 install virtualenv==20.0.23`  

create virtualenv  
`virtualenv .venv`  

activate the env  
`source .venv/bin/activate`  

### Create a new S3 bucket
install boto3  
`pip3 install boto3`  

run the script  
`create_hosted_bucket.py`  

