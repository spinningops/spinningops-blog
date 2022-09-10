#!/bin/bash


### Subnets Public
# subnet-03972e948b7f12410
# subnet-019117acca71626c8

### Subnets Private
# subnet-0a2c13d3291b18612
# subnet-0b890cff77e960d2e

### example to add multiple values
# ParameterKey=Subnets,ParameterValue=subnet-03972e948b7f12410\\,subnet-019117acca71626c8 \

# Upload CF Template
aws s3 cp infra-ecs-cluster.yaml s3://cf-templates-15pal9ojx6340-us-east-1/

# Update CF Stack
aws cloudformation update-stack --stack-name infra-ecs-cluster --template-url https://s3.amazonaws.com/cf-templates-15pal9ojx6340-us-east-1/infra-ecs-cluster.yaml \
    --parameters \
        ParameterKey=VPC,ParameterValue=vpc-0f341ca5a6a5c8dc7 \
        ParameterKey=EnvironmentName,ParameterValue=infra-ecs-cluster \
        ParameterKey=SecurityGroup,ParameterValue=sg-0f5e3c9f539b8260b \
        ParameterKey=Subnets,ParameterValue=subnet-02256f0fed087bdf4 \
        ParameterKey=KeyName,ParameterValue=ops \
        --capabilities CAPABILITY_NAMED_IAM