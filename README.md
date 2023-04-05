# aws-serverless-cloud-resume-challenge

## Setup
Create a new repo in github, clone locally. Download ths repo onto your machine, extract contents and paste them in your local github repo. Push all changes to the main branch of your repo and go through the errors one by one.

## Step 1:
The first failure is at the Configure AWS Credentials Step, our current role, does not have permissions to run aws commands in our account. You will need to create a role in your AWS account to be used.
![](https://i.ibb.co/ZLMGQT3/image.png)

Create a new role for this repository to have access to your AWS resources.
We created crc-serverless-role with the following trust policy corrections.
Add your repo into the StringLike condition like so: 

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
![](https://i.ibb.co/b260Tk0/image.png)

Now we are failing because there are no terraform files in the working directory. This is actually an error with how I copied all three repos into one. The ui, the api and the terraform repos. Now that all the code exsists in one repo, we have to make changes in the github workflow to allow the runner to be in the correct directory. This error will likely not show up for you.

from this:

````
permissions:
  id-token: write
  contents: read

defaults:
  run:
    shell: bash
    working-directory: .

jobs:

  deploy_production:
````

to this:

````
permissions:
  id-token: write
  contents: read

defaults:
  run:
    shell: bash
    working-directory: terraform

jobs:

  deploy_production:
````
  
## Step 3
![](https://i.ibb.co/v1Mrf6C/image.png)
This error is because github actions is trying to login to Terraform Cloud without credentials. Create a token, TF_API_TOKEN, in terraform cloud and add the token to your github secrets via https://developer.hashicorp.com/terraform/tutorials/automation/github-actions

<a href="https://ibb.co/RcTnhnb"><img src="https://i.ibb.co/TtMXKX2/image.png" alt="image" border="0"></a>

In this step we are also going to create an api driven workspace in terraform cloud and ensure we are naming it correctly in the main.tf file.

## Step 4
<a href="https://ibb.co/4jqTfS3"><img src="https://i.ibb.co/RCF0S6d/image.png" alt="image" border="0"></a>

This error is because github actions has detected terraforms environment variables. However, they are not set. You will need to set the following variables in TerraformCloud:

<a href="https://ibb.co/kgzPNFQ"><img src="https://i.ibb.co/QFhxyGr/image.png" alt="image" border="0"></a>

Ensure all the variables are in the terraform category. For the role variables you will have to create another role in AWS specifically for Terraform Cloud. 

Follow: https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services

Admin Policy:

<a href="https://ibb.co/wwG2GYR"><img src="https://i.ibb.co/KL484mX/image.png" alt="image" border="0"></a>

And the following trust relationship:

````
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::YOURACCOUNT:oidc-provider/app.terraform.io"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "app.terraform.io:aud": "aws.workload.identity"
                }
            }
        }
    ]
}
````

NOTE: you should not have to edit the trust policy after adding the admin policy to the role. This is shown here for completeness.

## Step 5
