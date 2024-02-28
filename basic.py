import boto3
k = boto3.resource("ec2")
k.create_instances(ImageId="ami-0e670eb768a5fc3d4", InstanceType="t2.micro", KeyName="	terraform-awskeypair", MaxCount=2, MinCount=1)

