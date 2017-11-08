# How to use VM
To access your instance:
1. Open an SSH client. (find out how to connect using PuTTY)

2. Locate your private key file (BotVMkey.pem). The wizard automatically detects the key you used to launch the instance.
3. Your key must not be publicly viewable for SSH to work. 
Use this command if needed:

chmod 400 BotVMkey.pem

4. Connect to your instance using its Public DNS:
ec2-18-220-170-51.us-east-2.compute.amazonaws.com

Example:
ssh -i "BotVMkey.pem" ubuntu@ec2-18-220-170-51.us-east-2.compute.amazonaws.com

Please note that in most cases the username above will be correct, however please ensure that you read your AMI usage instructions to ensure that the AMI owner has not changed the default AMI username.
