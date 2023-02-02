# Authenticate IAM credentials with awscli via MFA

## AWS config and credentials

edit `~/.aws/config` and add the new profile

```sh
[profile user1]
region=us-east-1
output=json

[profile user2]
region=us-east-1
output=json
```

edit `~/.aws.credentials` and add the new profile

```sh
[user1]
aws_access_key_id = <>
aws_secret_access_key = <>

[user2]
aws_access_key_id = <>
aws_secret_access_key = <>
```

## Linux

### Authenticate with mfa

this script will create or update new mfa profile and export the mfa profile to bash

start the script (with the dot)

- `. ./awscli-auth-with-mfa.sh`

### Switch profiles

if you need to switch between profiles

start the script (with the dot)

- `. ./awscli-switch-aws-profile.sh`

## Mac

### Authenticate with mfa

install `jq`

start the script (with the dot)

- `. ./awscli-auth-with-mfa.sh`
