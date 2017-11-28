# Deployment

We utilize [Ansible] (https://www.ansible.com/) as our configuration management tool. We launched a Amazon EC2 Ubutu 16.04 VM as the central server which is responsible for automate deployment of the machines that within its network.
For the purpose of testing, we launched two "clean" Amazon EC2 VMs (instance of Ubutu 16.04) that are to be deployed by our central VM. Following is our step-by-step deployment instruction.

## 1. Lanuch Amazon EC2 Ubuntu 16.40 VM:
If you are using a macOS, go to the directory that contain the file "BotVMkey.pem", then run one of the following command to ssh into the virtal machine:
* ssh -i "BotVMkey.pem" ubuntu@ec2-18-220-170-51.us-east-2.compute.amazonaws.com (Server, IP: 18.220.170.51)
* ssh -i "BotVMkey.pem" ubuntu@ec2-18-216-182-115.us-east-2.compute.amazonaws.com (Test, IP: 18.216.182.115)
* ssh -i "BotVMkey.pem" ubuntu@ec2-13-59-3-151.us-east-2.compute.amazonaws.com (Test, IP: 13.59.3.151)

## In Host Server Virtual Machine
### 2. Copy "BotVMkey.pem" from your computer to the server VM
Put the file in "home/ubuntu/" directory
```
scp -i "BotVMkey.pem" BotVMkey.pem ubuntu@ec2-18-220-170-51.us-east-2.compute.amazonaws.com:
```
### 3. Create Github SSH key pairs
Following instruction from github tutorial: [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
*When asked to set passphrase, hit enter to bypass it.*

Now you should have the following two files in your user directory
```
~/.ssh/id_rsa
~/.ssh/id_rsa.pub
```

### 4. Create an inventory file with the following content start with the IP address of the virtual machine
```
[nodes]
13.59.3.151 ansible_ssh_user=ubuntu ansible_ssh_private_key_file=./BotVMkey.pem
```
### 5. Create and edit the deployment script: [deploy.yml](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/deploy/deploy.yml)


```
vim deploy.yml
```
We will do the following tasks:

#### Set Environment Variables

```yml
   tasks:
    - name: Create env setting file
      command: touch /etc/profile.d/set_bot_env.sh
      become: yes
    - name: Set environment Variables
      lineinfile:
        dest: /etc/profile.d/set_bot_env.sh
        line: "export TEAM_NAME=510projectteam export BOARD_NAME='Demo Board' export BOT_TOKEN=xoxb-266498254006-btD2n1TcKdi5MY6AKlPGTwnm export BOT_ID=U7UEN7G06  export TRELLO_API_KEY=dbf6947f87a8dcb83f090731a27e8bd4 export TRELLO_API_SECRET=f57a6c66081742aa5f6149d329c3581d53231c308e4cc9f78b31230ce13b3bb8 export TRELLO_TOKEN=414df911de9e839c8ab9838c8fa1723107fba5848e5049269d88e5e94a348f31 export FIREBASE_API_KEY=AIzaSyCC5OzyEqGBcGZkpyUP90qUnyCCJY8SRQ8 export FIREBASE_AUTH_DOMAIN=taskmangerbot.firebaseapp.com export FIREBASE_DATABASE_URL=https://taskmangerbot.firebaseio.com export FIREBASE_STORAGE_BUCKET=taskmangerbot.appspot.com export GMAIL_ID=bot510project@gmail.com export GMAIL_PASS=simtiaz1234"
        insertafter: 'EOF'
        state: present
      become: yes
    - name: Copy setting.sh File for sourcing
      copy:
        src: /home/ubuntu/setting.sh
        dest: /home/ubuntu/setting.sh
    - name: Source the .bashrc file
      command: bash -lc "source .bashrc"
      become: yes
```

#### Install Packages
```yml
  vars:
    packages:
      - git
      - python-pip
      - python-setuptools
      - git-core
      - python-setuptools
      - debconf-utils
    pippackages:
      - slackclient
      - py-trello
      - pyrebase
      - python-firebase
   tasks:
    - name: Install packages
      apt:
        pkg: "{{ item }}"
        state: installed
        update_cache: yes
      with_items: "{{packages}}"
      become: yes
    - debug:
        msg: "{{ item }}"
      with_items: "{{packages}}"
    - name: PIP install python packages
      pip:
        name: "{{ item }}"
      with_items: "{{pippackages}}"
      become: yes

```
#### Clone Github Repo
```yml
  vars:
    dest_dir: /home/ubuntu/dev
    gh_repo: git@github.ncsu.edu:yhu22/CSC510_F17_Project.git
    gh_branch: 77d848d7cff464c9217b509e426ca8926437ee34
  tasks:
    - name: Copy ssh public key from server to client
      copy:
        src: /home/ubuntu/.ssh/id_rsa.pub
        dest: /home/ubuntu/.ssh/id_rsa.pub

    - name: Copy ssh private key from server to client
      copy:
        src: /home/ubuntu/.ssh/id_rsa
        dest: /home/ubuntu/.ssh/id_rsa

    - name: SSH Clone Github Repo
      git: repo={{ gh_repo }}
           version={{ gh_branch }}
           dest={{ dest_dir }}
           accept_hostkey=yes
           key_file="/home/ubuntu/.ssh/id_rsa"

```

(Github ssh key is located in this cotrol machine) 
#### Run Task Manager Bot
```yml
    - name: Run Task Manager Bot
      command: bash -lc "python dev/src/main.py"
      become: yes
```


### 6.Before run deploy.yml in server, make sure the to-be-deloyed machines have ansible installed already
Use the following command to install ansible:
```bash
sudo apt-get update
sudo apt-get install ansible 
```
## 7. Run deploy.yml with ansible to the targeted inventory 
```
ansible-playbook -i inventory deploy.yml
```

## Our results:



## Acceptance test instructions
Our project is integrating Trello board with the Slack, the Slack BOT will fetch the card information from Trello board and store them in the firebase database. Here, we provide [TA_account_info.txt](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/deploy/TA_account_info.txt) for TA to access our Demo Trello Board and our Slack Channel. (Firebase account included for the purpose to check database schema)

We have two virtual machine to demo our project.
