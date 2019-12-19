FROM python:3.6.9

RUN apt-get update && apt-get install -y python3-pip

# Add these as a separate layer as they get updated frequently
RUN pip3 install -U awscli boto3 aws-sam-cli aws-lambda-builders==0.0.4 --no-cache-dir