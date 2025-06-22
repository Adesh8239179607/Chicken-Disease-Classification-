import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotation
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    read yaml file and return 
    
    Args:
    path to yaml(str):path like input
    
    raises:
    ValueError: if yaml file is empty
    e:empty file
    
    Returns:
    ConfigBox: ConfigBox object with yaml content
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e    
    

@ensure_annotation
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create directories if they do not exist.
    
    Args:
    path_to_directories (list): List of directory paths to create.
    verbose (bool): If True, print the created directories.
    
    Returns:
    None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")



@ensure_annotation
def save_json(path: Path, data: Any):
    """
    Save data to a JSON file.
    
    Args:
    path (Path): Path to the JSON file.
    data (Any): Data to be saved in the JSON file.
    
    Returns:
    None
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)


    logger.info(f"Data saved to {path}")        


@ensure_annotation
def load_json(path: Path) -> ConfigBox:
    """
    Load data from a JSON file.
    
    Args:
    path (Path): Path to the JSON file.
    
    Returns:
    ConfigBox: data as class attribute intsead of dict.
    """
    with open(path) as f:
        content=json.load(f)

    
    logger.info(f"Json file  loaded from {path}")
    return ConfigBox(content)    


@ensure_annotation
def save_bin(data: Any, path: Path):
    """
    Save data to a binary file using joblib.
    
    Args:
    data (Any): Data to be saved.
    path (Path): Path to the binary file.
    
    Returns:
    None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotation
def load_bin(path: Path) -> Any:
    """
    Load data from a binary file using joblib.
    
    Args:
    path (Path): Path to the binary file.
    
    Returns:
    Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data    

@ensure_annotation
def get_size(path: Path) -> str:
    """
    Get the size of a file in bytes.
    
    Args:
    path (Path): Path to the file.
    
    Returns:
    int: Size of the file in kilo bytes.
    """
    size_in_Kb = round(os.path.getsize(path)/1024)
    
    return f"~ {size_in_Kb} KB"



def decodeImage(imgstring,fileName):
    """
    Decode a base64 encoded image string and save it as an image file.
    
    Args:
    imgstring (str): Base64 encoded image string.
    fileName (str): Name of the output image file.
    
    Returns:
    None
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """
    Encode an image file into a base64 string.
    
    Args:
    croppedImagePath (str): Path to the image file.
    
    Returns:
    str: Base64 encoded string of the image.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    


    