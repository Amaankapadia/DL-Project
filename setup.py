from setuptools import setup, find_packages

REQUIREMENTS_FILE = "requirements.txt"

def get_requirements_list():
    with open(REQUIREMENTS_FILE, 'r') as f:
        return f.read().splitlines()

setup(
    name="cnnClassifier",
    version="0.0.1",
    author="Amaan",
    description="A CNN classifier project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements_list()
)