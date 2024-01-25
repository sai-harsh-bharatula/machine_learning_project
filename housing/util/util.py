import yaml
import os, sys
from housing.exception import exceptionHousing



def readYAMLFile(file_path: str)->dict:
    """
    This function reads a YAML file and returns the contents in the form of dictionary
    file_path: str 
    """
    try:
        with open(file_path, "rb") as YAML_file:
            return yaml.safe_load(YAML_file)
    except Exception as e: 
        raise exceptionHousing(e, sys) from e

