import os

from numpy import size
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging.logger import logging
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns it as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Returns:
        ConfigBox: ConfigBox object containing the yaml data.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they don't exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Directory created at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of the file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

