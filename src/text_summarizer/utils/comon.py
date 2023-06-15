import os
from box.exceptions import BoxValueError
import yaml
from text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox 
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_ymal:Path)->ConfigBox:
    # return ConfigBox()
    """
        reads yaml file and returns

        Args:
        path_to_ymal (str): path like input

        Raises:
            ValueError: if yaml file is empty
            e: empty file

        Returns:
            ConfigBox: ConfigBox type object    
    """
    try:
       with open(path_to_ymal) as yaml_file:
            print(content)
            content = yaml.safe_load(yaml_file)
            # print(type(content))
            # print(ConfigBox(content))
            # print(type(ConfigBox(content)))
            logger.info(f"yaml file: {path_to_ymal} loaded successfully")
            return ConfigBox(content)
      
        # print("IN READ YAML FUN",path_to_ymal)
        # with open(path_to_ymal) as f:
        #     content = yaml.safe_load(f)
        # logger.info(f"yaml fole: {path_to_ymal} lodded successfully")
        # print(ConfigBox(content) )
        # return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
       
    except yaml.YAMLError as exc:
        print(exc)
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
        create list of directories

        Args: 
            path_to_directories (list): list of path of directories
            ignore_log (bool,optional): ignore if multiple directories to be created. Default is False
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory: {path}")


@ensure_annotations
def get_size(path:Path) -> str:
    """
        get size in KB

        Args:
            path(Path): path of the file
        Returns:
            str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


