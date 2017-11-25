# Deployment

## Lanuch two Amazon EC2 Ubuntu 16.40 Virtual machine for testing:
The deployment scripts we write will be located in one of the virtual machine and install all the requirement in the second virtual machine and run our bot in the second virtual machine automatically.


document how these configuration management tools and deployment scripts should be run and make sure to include demonstrate running them in your screencast.

* ubuntu@ip-172-31-31-155: controller 18.216.182.115
* ubuntu@ip-172-31-32-179: target machine 18.220.170.51

## deploy_bot.yml

Install ansible in both of the virtual machine
* ssh -i "BotVMkey.pem" ubuntu@ec2-18-216-182-115.us-east-2.compute.amazonaws.com
* ssh -i "BotVMkey.pem" ubuntu@ec2-18-220-170-51.us-east-2.compute.amazonaws.com
* ssh -i "BotVMkey.pem" ubuntu@ec2-18-217-117-252.us-east-2.compute.amazonaws.com (Test) 18.217.117.252



## In Host Server Virtual Machine
1. Create an inventory file with the following content
```
[nodes]
18.217.117.252 ansible_ssh_user=ubuntu ansible_ssh_private_key_file=./BotVMkey.pem
```
## In a machine that we will deployed
### Prerequisite: The machine has ansible installed already
```bash
sudo apt-get update
sudo apt-get install ansible 
```

## Acceptance test instructions


Trello

Slack
