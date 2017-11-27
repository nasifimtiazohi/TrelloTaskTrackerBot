# Deployment

## Lanuch two Amazon EC2 Ubuntu 16.40 Virtual machine for testing:
The deployment scripts we write will be located in one of the virtual machine and install all the requirement in the second virtual machine and run our bot in the second virtual machine automatically.


document how these configuration management tools and deployment scripts should be run and make sure to include demonstrate running them in your screencast.

* ubuntu@ip-172-31-31-155: controller 18.216.182.115
* ubuntu@ip-172-31-32-179: target machine 18.220.170.51

## deploy_bot.yml

Install ansible in both of the virtual machine
* ssh -i "BotVMkey.pem" ubuntu@ec2-18-220-170-51.us-east-2.compute.amazonaws.com (Server, IP: 18.220.170.51)
* ssh -i "BotVMkey.pem" ubuntu@ec2-18-216-182-115.us-east-2.compute.amazonaws.com (Test, IP: 18.216.182.115)
* ssh -i "BotVMkey.pem" ubuntu@ec2-18-217-117-252.us-east-2.compute.amazonaws.com (Test, IP: 18.217.117.252) (cannot start)
* ssh -i "BotVMkey.pem" ubuntu@ec2-13-59-3-151.us-east-2.compute.amazonaws.com (Test, IP: 13.59.3.151)



## In Host Server Virtual Machine
1. Create an inventory file with the following content
start with the IP address of the virtual machine
```
[nodes]
13.59.3.151 ansible_ssh_user=ubuntu ansible_ssh_private_key_file=./BotVMkey.pem
```

2. Run deployment code
```
ansible-playbook -i inventory deploy.yml
```
## In a machine that we will deployed
### Prerequisite: The machine has ansible installed already
```bash
sudo apt-get update
sudo apt-get install ansible 
```

## Acceptance test instructions
Our project is integrating Trello board with the Slack, the Slack BOT will fetch the card information from Trello board and store them in the firebase database. Here, we provide [TA_account_info.txt](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/deploy/TA_account_info.txt) for TA to access our Demo Trello Board and our Slack Channel. (Firebase account included for the purpose to check database schema)

We have two virtual machine to demo our project.
