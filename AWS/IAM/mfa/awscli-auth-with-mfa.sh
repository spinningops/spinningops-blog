#!/bin/bash
set -e

echo "Hi, Please add your AWS account id"
read ACCOUNT_ID

echo "Please add your IAM username"
read MFA_USER

echo "Please add your 6-digit code from google authenticator"
read MFA_TOKEN

TOKEN=$(aws sts get-session-token --duration-seconds 3600 --serial-number arn:aws:iam::$ACCOUNT_ID:mfa/$MFA_USER --token-code $MFA_TOKEN)

# write output to temp json file
echo $TOKEN > temp-token.json

# assign temp creds to vars
TEMP_ACCESS_ID=$(jq -r '.Credentials | .AccessKeyId' temp-token.json)
TEMP_SECRET=$(jq -r '.Credentials | .SecretAccessKey' temp-token.json)
TEMP_TOKEN=$(jq -r '.Credentials | .SessionToken' temp-token.json)

# set temp creds in aws/credentials
aws configure set aws_access_key_id $TEMP_ACCESS_ID --profile mfa
aws configure set aws_secret_access_key $TEMP_SECRET --profile mfa
aws configure set aws_session_token $TEMP_TOKEN --profile mfa

# cleanup
rm temp-token.json

echo "Access token is ready! If you need to switch AWS_PROFILE use the script awscli-switch-aws-profile.sh"
echo "default profile is "$AWS_PROFILE