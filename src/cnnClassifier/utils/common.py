import os  
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from src.cnnClassifier import logger 
import json 
import joblib 
from ensure import ensure_annotations
from typing import Any
import base64 
from pathlib import Path 

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and returns 
    
    Args:
         path_to_yaml (Path): path like input
         
    raises: 
         ValueError : if yaml file is empty 
         e : empty file 
         
    Returns: 
        ConfigBox : ConfigBox type"""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list,verbose = True): 
    """create list of directories 
    
    Args:
        path_to_directories (list[Path]): list of path of directories
    """
    for path_to_directory in path_to_directories:
        os.makedirs(path_to_directory, exist_ok=True)
        if verbose : 
            logger.info(f"created directory at : {path_to_directory}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save dict as json file 
    
    Args:
        path (Path): path to json file 
        data (dict): data to be saved 
    """
    with open(path,"w") as json_file:
        json.dump(data,json_file,indent=4)

    logger.info(f"json file saved at : {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file and returns 
    
    Args:
         path (Path): path like input
         
    raises: 
         e : empty file 
         
    Returns: 
        ConfigBox : ConfigBox type"""
    with open(path) as json_file:
        content = json.load(json_file)
        logger.info(f"json file: {path} loaded successfully")
        return ConfigBox(content)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file 
    
    Args:
        data (Any): data to be saved 
        path (Path): path to binary file 
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at : {path}") 

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary file 
    
    Args:
        path (Path): path to binary file 
        
    Returns:
        Any: data loaded from binary file 
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from : {path}") 
    return data 

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path to file 
        
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB" 

@ensure_annotations
def decodeImage(imgstring,filename):
    """Decode a base64 string and save it as an image file.
    
    Args:
        imgstring (str): The base64 encoded string representing the image.
        filename (str): The path where the decoded image will be saved.
    """
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
    logger.info(f"Image saved to {filename}")

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    """Encode an image file into a base64 string.
    
    Args:
        imagePath (Path): The path to the image file to be encoded.
        
    Returns:
        str: The base64 encoded string representing the image.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read()) 

