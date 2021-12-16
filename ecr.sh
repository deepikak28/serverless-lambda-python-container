#!/bin/bash

region=ap-southeast-2
local_image=hello-world:latest
aws_account=<aws_account_id>
ecr_image=hello-world:latest
profile=<aws_profile>

docker build -t $local_image .

aws ecr get-login-password --region $region --profile $profile  | docker login --username AWS --password-stdin $aws_account.dkr.ecr.$region.amazonaws.com

aws ecr create-repository --repository-name hello-world --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE --profile $profile --region $region

docker tag $local_image $aws_account.dkr.ecr.$region.amazonaws.com/$ecr_image

docker push $aws_account.dkr.ecr.$region.amazonaws.com/$ecr_image