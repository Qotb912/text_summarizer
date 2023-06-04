import os
import urllib.request as req
import zipfile
from pathlib import Path
from text_summarizer.entity import DataIngestionConfig
from text_summarizer.logging import logger
from text_summarizer.utils.comon import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = req.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded successfully with following info: \n{header}")
        else:
            logger.info(f"File already exists of size:{get_size(Path(self.config.local_data_file))}")


    def etract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file , 'r') as zip_f:
            zip_f.extractall(unzip_path)
 