# aws-serverless-cloud-resume-challenge

## Setup
Create a new repo in github, clone locally. Download ths repo onto your machine, extract contents and paste them in your local github repo. Push all changes to the main branch of your repo and go through the errors one by one.

## Step 1:
![picture alt](https://ibb.co/QC3Cdv2)  
> Create a new role for this repository to have access to your AWS resources.
> We created crc-serverless-role with the following trust policy corrections:
> Add your repo into the StringLike condition like so: 

````
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::198516399747:oidc-provider/token.actions.githubusercontent.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "token.actions.githubusercontent.com:sub": "repo:kcelestine/aws-serverless-cloud-resume-challenge:*",
                    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
                }
            }
        }
    ]
}
````

> arn:aws:iam::198516399747:role/crc-serverless-role
> Now copy this arn into the github workflow and wait for the next error.

## Step 2:
