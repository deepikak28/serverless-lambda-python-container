# Deploy Lambda from container image with Serverless Framework

<br>

# Prerequisites

* **Docker**
* **Serverless Framework**
* **AWS Account**: Services Used:
    * AWS Lambda
    * AWS ECR
    * AWS API Gateway
* **AWS CLI Configuration**

<br>

## Hello World Python Container on Lambda

1. lambda.py - Contains your business logic
2. Dockerfile - to build the container image 

## Step1 - Create the Container Image and push it to ECR



1. Build the Dockerfile and Tag the image

    Run the ./ecr.sh script in the root folder (It will build the image, create ECR repo, tag the image and push the docker image to ECR repository)

    Alternatively, you can take the manual steps described below.

    ## OR

    ```
    docker build -t hello-world:latest .
    docker tag hello-world:latest <account_id>.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest

    ```
    2. Create ECR repository and Push the image

    ```
    aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
    aws ecr create-repository --repository-name <repo-name> --image-scanning-configuration scanOnPush=true --region <region>
    docker push <account_id>.dkr.ecr.<region>.amazonaws.com/hello-world:latest

    ```
# Step2 - Deploy the serverless stack for creating the lambda and protected API with API keys.

    Now our image is pusged to the repository, we will create a protected API backed by lambda with serverless framework. The prerequisite here is to have serverless installed on your machine.

    1. Go to the root folder and deploy the serverless stack

        ```
        sls deploy --stage <stage> --region <region>
        ```
    2. Once stack is deployed, it will create the AWS resources and provide you the API key to access your API endpoint.


# If you are using Cognito or any other IdP you can use Cognito Authorizer or Custom authorizers rather than API keys.
        
