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

'''bash 
https://github.com/Amaankapadia/DL-Project.git
''' 

### STEP 01: CREATE A ENVIRONMENT AFTER OPENING THE REPOSITORY 

python -m venv chicken 

source chicken/Scripts/activate 

### STEP 02: INSTALL THE REQUIREMENTS 

pip install -r requirements.txt 

### STEP 03: RUN THE APPLICATION 

python app.py 

### STEP 04: TRAIN YOUR MODEL 

# Can be done in 2 ways:

# 1. Run through DVC
dvc repro

# 2. Run through main.py
python main.py

### DVC COMMANDS 

dvc init
dvc repro
dvc dag

### MLflow and DVC

 - MLflow
 - DVC

### About the Project
This project is designed to help poultry farmers and veterinarians quickly identify Coccidiosis in chickens through image analysis. The system achieves:

Training Accuracy: 86.82%
Validation Accuracy: 89.06%
Test Accuracy: 93.10%
The web interface allows users to upload chicken images and get instant predictions about the presence of Coccidiosis.

### AWS Deployment
The application can be deployed on AWS EC2 instance for production use.

### Tech Stack Used
Python 3.8+
TensorFlow
DVC
Flask
AWS

### Author
Amaan Kapadia
Email: amaankapadiaak2@gmail.com
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

