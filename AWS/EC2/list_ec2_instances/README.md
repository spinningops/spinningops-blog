# List EC2 instances of entire aws account

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

### List EC2 instances from all regions
Install awscli     
`pip3 install awscli`   

Run the script  
`list_ec2_instances.sh`  

Got this sh script from this gist:       
https://gist.github.com/junaidk/433345da5bf8e580680d9109792d3169
