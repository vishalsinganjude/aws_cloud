# Welcome To AWS CLI - Create instance by using commands
## How to create EC2 instances just follow below steps :
### 1. Create a key-pair for instance :
    > aws ec2 create-key-pair --key-name 'keyname' --query 'KeyMaterial' --output text > keyname.pem
### 2. Create Security Group :
    > aws ec2 create-security-group --group-name "Write down security group name" --description "My First Security Group" --vpc-id **vpc-7a7d7100**
    for vpc-id go to aws console and search vpc service
### 3. Adding Rule in AWS Groups :
    > aws authorize-security-group-ingress --group-id "write down created group id" --protocol tcp --port 22 --cidr 103.73.212.162
    group_id : go to aws console search ec2 in that u will able to see security group
    --cidr 103.73.212.162 : go to http://checkip.amazonaws.com/
### 4. Finally Create instance 
    > aws ec2 run-instances --image-id ami-0323c3dd2da7fb37d --count 1 --instance-type t2.micro 
    --key-name vishal --security-group-ids sg-089dc298e69b74646 --subnet-id subnet-c278f88f
    ami-0323c3dd2da7fb37d : go to ec2 launch instances there u will get copy and paste here
    t2.micro : after selecting image-id go inside u will get this name  (--instance-type)
    vishal : Your created key-name 
    sg-089dc298e69b74646 : Your created group id
    --subnet-id subnet-c278f88f : for this goto subnet in that u will get available zones select any one

### To set the Permission
    > chmod 400 keyName.pem
    > ssh -i vishal.pem ec2-user@3.87.179.26
    3.87.179.26 : go to running instance - start your instance in below that u will shown 
    IPv4 Public IP : 3.87.179.26 copy this 
    vishal.pem : keyName
## Done
# Example : 
### 1. Create a key-pair for instance :
![IMG-20200504-WA0016](https://user-images.githubusercontent.com/29985801/81040304-b89b2480-8ec8-11ea-8afa-2e91259a83c1.jpg)
    
    To check key was create or not got to aws console key-pairs and check :
![IMG-20200504-WA0015](https://user-images.githubusercontent.com/29985801/81040424-f13afe00-8ec8-11ea-8c05-2ab5c9d34138.jpg)
### 2. Create Security Group
    First check your vpc-id :
![vpcs](https://user-images.githubusercontent.com/29985801/81041630-f188c880-8ecb-11ea-87cb-74273f924d3e.jpeg)
    
    Then insert below command and put there above vpc-id :

![IMG-20200504-WA0007](https://user-images.githubusercontent.com/29985801/81040704-8dfd9b80-8ec9-11ea-99a0-c2502217c2fd.jpg)

    To check Group-id is created or not go to ec2 - security group and check :
![IMG-20200504-WA0012](https://user-images.githubusercontent.com/29985801/81040775-c309ee00-8ec9-11ea-83a5-21754efada96.jpg)

### 3. Adding Rule in AWS Groups :
    Before type command fisrt go to browser and search : http://checkip.amazonaws.com/ here u got ip then go for command
![IMG-20200504-WA0005](https://user-images.githubusercontent.com/29985801/81040916-154b0f00-8eca-11ea-9415-c592d2423ed3.jpg)

### 4. Finally Create instance 
    First of all go to browser shown in below - go to launch instances :
![IMG-20200504-WA0008](https://user-images.githubusercontent.com/29985801/81042153-1a5d8d80-8ecd-11ea-9e6f-6cb4ded2e8e6.jpg)

    After that U shown below image - select any os u want and copy image-id :
![IMG-20200504-WA0014](https://user-images.githubusercontent.com/29985801/81042269-601a5600-8ecd-11ea-8e05-baaed02ae637.jpg)

    After that click to (select) then u shown below image - here u get instance-tpye any one u want and 
    copy there instance-type :
![IMG-20200504-WA0011](https://user-images.githubusercontent.com/29985801/81042392-a40d5b00-8ecd-11ea-8b68-1e94ee719f57.jpg)

    After that check subnet-id - below in vpc id choose any id (its a available zone for u) :
![IMG-20200504-WA0010](https://user-images.githubusercontent.com/29985801/81042661-3ca3db00-8ece-11ea-874a-9b812ec3bf33.jpg)

    When u get all ids copy all in notepad after that type below command to create and run instance :

![IMG-20200504-WA0009](https://user-images.githubusercontent.com/29985801/81042844-a7edad00-8ece-11ea-9d0a-4c263e6857f4.jpg)

    Check Your instance is create and Running or not - goto browser ec2 - running instances :
![IMG-20200504-WA0006](https://user-images.githubusercontent.com/29985801/81042803-8e4c6580-8ece-11ea-9368-70db72f59c9a.jpg)


### To set the Permission
    Goto command prompt and type below commands :
    > chmod 400 keyName.pem
    > ssh -i vishal.pem ec2-user@3.87.179.26
    3.87.179.26 : go to running instance - start your instance in below that u will shown 
    IPv4 Public IP : 3.87.179.26 copy this 
    vishal.pem : keyName