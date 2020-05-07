# Steps to create and start instance by using API Gateway (through Link)
### 1. Create Key-pair
### 2. Create lambda Function
    > Create Function
    > Author from scratch
        > Name : AnyName
        > Runtime : choose any language
        > Role : Create a Custom Role
    > Expand choose or create an Execution Role :
        > Choose create a new Role with basic lambda permissions
    > Create Function.
### 3. Goto IAM 
    > Click on Role
    > Select Role and click on name (Eg. YourFunctioname........ lambda).
    > Click on Policy.
    > Click on JSON.
        > Edit Policy > JSON
        > paste JSON code (check jsonPolicy.txt)
        > Review Policy and Save Changes.
### 4. Return To lambda Function 
    > write code (check CreateEC.py)
    > Scroll down to the Environment variables section
        > Click on Edit (right side corner)
        > Click on add Environment Variable (key : value pair)
              KEY               VALUE
            > AMI            :  image-id
            > INSTANCE_TYPE  :  t2.micro (any u want)
            > KEY_NAME       :  YourKeyName
            > SUBNET_ID      :  YourAvailableSubnet-id
        > Click on Save
    > Save Function
### 5. Click on test
    > Event Template as it is (hello-world don't change)
    > Event Name (Any)
    > In code fill blank (delete all) : put only { }
        > { }
    > Click on Create.
### Now You can check Your Function is working or not 
    > click on test
    > U will get Output in (Execution block)
    > to check goto EC2 instance and check your instance is create or not.
# Done !!!
### Now Create API Gateway for your lambda function so u can click on link and your instance is create so lets do that 
### $ Follow Below Steps :
    > Goto Services - Search API Gateway (open in new tab) 
    > Click on Create API
    > HTTP API 
        > Click on Build
    > In Integration Choose 
        > lambda
    > lambda function - Choose your created labda function here.
    > API_NAME : Any name u want
    > Click on Next
    > on Method Choose - Get
    > Click On Next
    > Configure Stages 
        > Stage name : $default (auto deploy - enabled )
    > Click on Next
    > review and click on Create
    > Copy link (check in Invoke url ) and paste any blank tab
    > Goto Route on left hand side (Copy your route and paste at the end of link eg. link/routename)
### when u click that link u will get null message on your window.
    (Thats means your instance successfully Created)
    > Now Check Your instance and u will get ur instance is create and start.
# Congratulations !! Your hands on lab ..
 # Example for above steps : 
 
 ## 1. Create Key if u don't have ( Follow below steps ) :
![WhatsApp Image 2020-05-07 at 1 17 32 PM](https://user-images.githubusercontent.com/29985801/81270677-ba9be980-9068-11ea-90be-2c9c26bd8eb3.jpeg)
![WhatsApp Image 2020-05-07 at 1 17 31 PM](https://user-images.githubusercontent.com/29985801/81270696-c1c2f780-9068-11ea-9bc4-ac987ee2353f.jpeg)
![WhatsApp Image 2020-05-07 at 1 13 35 PM (1)](https://user-images.githubusercontent.com/29985801/81270712-c7204200-9068-11ea-9e54-4c21452f14f7.jpeg)
![WhatsApp Image 2020-05-07 at 1 13 35 PM](https://user-images.githubusercontent.com/29985801/81270718-c9829c00-9068-11ea-9746-5b8c26645a6c.jpeg)

## 2. Create lambda Function ( Follow below steps ) :

![WhatsApp Image 2020-05-07 at 1 13 34 PM (2)](https://user-images.githubusercontent.com/29985801/81271032-2ed68d00-9069-11ea-97bb-bf3f08958c99.jpeg)

    > Click on Create Function ( right side corner ) Then follow Below steps :
![WhatsApp Image 2020-05-07 at 1 13 34 PM](https://user-images.githubusercontent.com/29985801/81271359-9ab8f580-9069-11ea-9dc5-97ade8b8c6ec.jpeg)
    
    > paste Below code to console :
    import os
    import boto3
    
    AMI = os.environ['AMI']
    INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
    KEY_NAME = os.environ['KEY_NAME']
    SUBNET_ID = os.environ['SUBNET_ID']
    ec2 = boto3.resource('ec2')
    def lambda_handler(event, context):
        instance = ec2.create_instances(
            ImageId=AMI,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            SubnetId=SUBNET_ID,
            MaxCount=1,
            MinCount=1
        )
        print("New instance created:", instance[0].id)
![WhatsApp Image 2020-05-07 at 1 13 33 PM (1)](https://user-images.githubusercontent.com/29985801/81271383-a1476d00-9069-11ea-8842-bdbb94d65f51.jpeg)
    
    > Click On Create Function then Check your function is created successfully.

![WhatsApp Image 2020-05-07 at 1 13 28 PM](https://user-images.githubusercontent.com/29985801/81273127-14ea7980-906c-11ea-9552-2eeb7553e8af.jpeg)
 
### 3. Goto IAM and Follow Below Steps :

![WhatsApp Image 2020-05-07 at 1 13 30 PM (1)](https://user-images.githubusercontent.com/29985801/81273490-92ae8500-906c-11ea-9a11-f78686047c47.jpeg)
![WhatsApp Image 2020-05-07 at 1 13 30 PM](https://user-images.githubusercontent.com/29985801/81273509-98a46600-906c-11ea-96df-3084c0c806df.jpeg)
![WhatsApp Image 2020-05-07 at 1 13 29 PM (1)](https://user-images.githubusercontent.com/29985801/81273519-9cd08380-906c-11ea-83c6-701cdb396c56.jpeg)
    
        > Click on JSON.
        > Edit Policy > JSON
        > paste Below JSON code on policies console:
            {
                "Version": "2012-10-17",
                "Statement": [{
                  "Effect": "Allow",
                  "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                    ],
                "Resource": "arn:aws:logs:*:*:*"
                },
                {
                    "Action": [
                    "ec2:RunInstances"
                    ],
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ]
        }
        > Review Policy and Save Changes.
![WhatsApp Image 2020-05-07 at 1 13 29 PM](https://user-images.githubusercontent.com/29985801/81273529-a0fca100-906c-11ea-9f8b-9036dc439a8b.jpeg)

### 4. Return To lambda Function and Follow below Steps :
    > Scroll down 
![WhatsApp Image 2020-05-07 at 1 13 33 PM](https://user-images.githubusercontent.com/29985801/81274498-feddb880-906d-11ea-9a39-3ac4a5cf8b7b.jpeg)
![WhatsApp Image 2020-05-07 at 1 13 32 PM (1)](https://user-images.githubusercontent.com/29985801/81274506-03a26c80-906e-11ea-8c4e-77e96925d8f3.jpeg)

    To check :
        > AMI : goto services (Search) - EC2 (Open in new tab) - click on launch instances (Copy id)
![WhatsApp Image 2020-05-07 at 1 13 32 PM](https://user-images.githubusercontent.com/29985801/81275059-c1c5f600-906e-11ea-8524-1e14ea45f468.jpeg)
    
        > INSTANCE_TYPE : also find on second step of launch instance (goto second step ) (Copy type)
![WhatsApp Image 2020-05-07 at 1 13 31 PM (2)](https://user-images.githubusercontent.com/29985801/81275064-c5f21380-906e-11ea-9f35-3f068643ceaf.jpeg)

        > KEY_NAME : YourKeyAboveCreated (Write key name here)
        > SUBNET_ID : To check available zone - goto services ( Search ) - VPC (Open in new tab) : 
        (Copy any one id and paste here )
![WhatsApp Image 2020-05-07 at 12 31 40 PM](https://user-images.githubusercontent.com/29985801/81275547-79f39e80-906f-11ea-961b-3a4da042f15f.jpeg)

    > Click on Save
![WhatsApp Image 2020-05-07 at 1 13 31 PM](https://user-images.githubusercontent.com/29985801/81274544-13ba4c00-906e-11ea-8842-15af723d2e65.jpeg)

### 5. Click on test
    > Event Template as it is (hello-world don't change)
    > Event Name (Any)
    > In code fill blank (delete all) : put only { }
        > { }
    > Click on Create.
![WhatsApp Image 2020-05-07 at 1 13 28 PM (1)](https://user-images.githubusercontent.com/29985801/81275996-0aca7a00-9070-11ea-8a68-9b3de22267ae.jpeg)

### Now You can check Your Function is working or not 
    > click on test
    > U will get Output in (Execution block)
![WhatsApp Image 2020-05-07 at 2 41 32 PM](https://user-images.githubusercontent.com/29985801/81276636-e8852c00-9070-11ea-91ce-37279d1fdcc1.jpeg)

    > to check goto EC2 instance and check your instance is create or not.
# Done !!!

### 6. Now Create API Gateway ( Follow Bellow Steps ) :
    > Goto Services - Search API Gateway (open in new tab)
![WhatsApp Image 2020-05-07 at 2 51 05 PM](https://user-images.githubusercontent.com/29985801/81277615-48300700-9072-11ea-8f0d-3b03d8a26fa2.jpeg)

![WhatsApp Image 2020-05-07 at 1 13 27 PM](https://user-images.githubusercontent.com/29985801/81278112-e15f1d80-9072-11ea-9a3a-fd0d5797f410.jpeg)

![WhatsApp Image 2020-05-07 at 1 13 26 PM (1)](https://user-images.githubusercontent.com/29985801/81277742-744b8800-9072-11ea-996b-f3ce0ea759c3.jpeg)

![WhatsApp Image 2020-05-07 at 1 13 26 PM (2)](https://user-images.githubusercontent.com/29985801/81277760-7ad9ff80-9072-11ea-9742-769bfe0c0c35.jpeg)

![WhatsApp Image 2020-05-07 at 1 13 25 PM](https://user-images.githubusercontent.com/29985801/81277837-93e2b080-9072-11ea-9917-6fa0fbbaece1.jpeg)

![WhatsApp Image 2020-05-07 at 1 13 26 PM](https://user-images.githubusercontent.com/29985801/81278088-d906e280-9072-11ea-9689-51173497b9e5.jpeg)

![WhatsApp Image 2020-05-07 at 12 37 24 PM (1)](https://user-images.githubusercontent.com/29985801/81278228-03f13680-9073-11ea-8385-d68260a58ab7.jpeg)
    
![WhatsApp Image 2020-05-07 at 12 37 22 PM](https://user-images.githubusercontent.com/29985801/81278244-081d5400-9073-11ea-813a-572af71b3af8.jpeg)

![WhatsApp Image 2020-05-07 at 12 37 22 PM (1)](https://user-images.githubusercontent.com/29985801/81278277-14a1ac80-9073-11ea-8550-de93c48cfbdd.jpeg)

    > Now You can click Your link
    > Go to EC2 - running instances 
# Congratulations Your one Tap link is created Successfully by using API and Lambda !!

## Now For local goto security groups - create inbound Rule
    
![WhatsApp Image 2020-05-07 at 12 37 23 PM](https://user-images.githubusercontent.com/29985801/81285744-9a2a5a00-907d-11ea-8156-f273803494ce.jpeg)

![WhatsApp Image 2020-05-07 at 12 37 24 PM](https://user-images.githubusercontent.com/29985801/81285748-9c8cb400-907d-11ea-8e46-3389643b403c.jpeg)
    
 # Goto Local command prompt
    > goto that folder where ur key-pair is saved.
   
    $ chmod 400 <KEY PAIR>.pem
    # Replace <KEY-PAIR> with your key pair name.
    
    $ ssh -i <KEY-PAIR>.pem ec2-user@<IP ADDRESS>
    # Remember to replace <IP ADDRESS> with the public IP of the EC2 instance you created.
    
