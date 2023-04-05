# aws-serverless-cloud-resume-challenge

## Setup
Create a new repo in github, clone locally. Download ths repo onto your machine, extract contents and paste them in your local github repo. Push all changes to the main branch of your repo and go through the errors one by one.

## Step 1:
The first failure is at the Configure AWS Credentials Step, our current role, does not have permissions to run aws commands in our account. You will need to create a role in your AWS account to be used.
![](https://i.ibb.co/gPLPVZ5/1.png)

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

