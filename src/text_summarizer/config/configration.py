from text_summarizer.constants import *
from text_summarizer.utils.comon import read_yaml, create_directories
from text_summarizer.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
            self,
            config_file_path = PROJECT_DIR.joinpath( CONFIG_FILE_PATH),
            params_file_path = PROJECT_DIR.joinpath(PARAMS_FILE_PATH)):
        
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
       

        create_directories([PROJECT_DIR.joinpath(self.config.artifacts_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
       
        create_directories([PROJECT_DIR.joinpath(config.root_dir)])  
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = PROJECT_DIR.joinpath( config.root_dir),
            source_URL =  config.source_URL,
            local_data_file = PROJECT_DIR.joinpath( config.local_data_file),
            unzip_dir = PROJECT_DIR.joinpath( config.unzip_dir)
        )
        
        return data_ingestion_config
 