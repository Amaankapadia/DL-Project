# DL-Project 

## Workflows 

1. Update config.yaml 
2. Update secrets.yaml(optional) 
3. Update params.yaml 
4. Update the entity 
5. Update the configuration manager in src 
6. Update the components 
7. Update the pipeline 
8. Update the main.py 
9. Update the dvc.yaml 

## PROJECT STRUCTURE 

DL-Project/
├── artifacts/
│ ├── data_ingestion/
│ │ └── Chicken fickle images/
│ ├── prepare_base_model/
│ │ ├── base_model.h5
│ │ └── updated_base_model.h5
│ ├── prepare_callbacks/
│ │ ├── checkpoint_dir/
│ │ │ └── model.h5
│ │ └── tensorboard_log_dir/
│ └── training/
│ └── model.h5
├── config/
│ └── config.yaml
├── research/
│ ├── 01_data_ingestion.ipynb
│ ├── 02_prepare_base_model.ipynb
│ ├── 03_prepare_callbacks.ipynb
│ ├── 04_training.ipynb
│ └── 05_model_evaluation.ipynb
├── src/
│ └── cnnClassifier/
├── templates/
│ └── index.html
├── app.py
├── dvc.yaml
├── params.yaml
└── setup.py

## How to run? 

### STEPS: 

clone the repository 

```bash
https://github.com/Amaankapadia/DL-Project.git
```

### STEP 01: CREATE A ENVIRONMENT AFTER OPENING THE REPOSITORY 
```bash
python -m venv chicken 
```
```bash
source chicken/Scripts/activate 
```
### STEP 02: INSTALL THE REQUIREMENTS 

```bash
pip install -r requirements.txt 
```
### STEP 03: RUN THE APPLICATION 

```bash
python app.py 
```
### STEP 04: TRAIN YOUR MODEL 

# Can be done in 2 ways:

1. Run through DVC
dvc repro

2. Run through main.py
python main.py

# DVC COMMANDS 

dvc init
dvc repro
dvc dag

# MLflow and DVC

 - MLflow
 - DVC

# About the Project
This project is designed to help poultry farmers and veterinarians quickly identify Coccidiosis in chickens through image analysis. The system achieves:

Training Accuracy: 86.82%
Validation Accuracy: 89.06%
Test Accuracy: 93.10%
The web interface allows users to upload chicken images and get instant predictions about the presence of Coccidiosis.

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6


## Run from terminal:

docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run


# Tech Stack Used
Python 3.8+
TensorFlow
DVC
Flask
AWS

# Author

Amaan Kapadia

Email: amaankapadia78692@gmail.com

GitHub: @Amaankapadia 


You can now copy this entire content and paste it into your README.md file. The formatting is already done with proper Markdown syntax, including:
- Headers with different levels
- Code blocks with syntax highlighting
- Lists (both ordered and unordered)
- Links
- Project structure tree
- Command examples
- Performance metrics
- Contact informationYou can now copy this entire content and paste it into your README.md file. The formatting is already done with proper Markdown syntax, including:
- Headers with different levels
- Code blocks with syntax highlighting
- Lists (both ordered and unordered)
- Links
- Project structure tree
- Command examples
- Performance metrics
- Contact information

