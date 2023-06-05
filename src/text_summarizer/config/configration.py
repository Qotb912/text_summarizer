from text_summarizer.constants import *
from text_summarizer.utils.comon import read_yaml, create_directories
from text_summarizer.entity import DataIngestionConfig, DataTransformationConfig , DataValidationConfig


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
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([PROJECT_DIR.joinpath(config.root_dir)])
        data_validation_config = DataValidationConfig(
            root_dir= PROJECT_DIR.joinpath( config.root_dir),
            STATUS_FILE= PROJECT_DIR.joinpath( config.STATUS_FILE),
            ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES,
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([PROJECT_DIR.joinpath( config.root_dir)])
        print(type(config))
        data_transformation_config = DataTransformationConfig(
            root_dir= PROJECT_DIR.joinpath(config.root_dir),
            data_path= PROJECT_DIR.joinpath(config.data_path),
            tokenizer_name= config.tokenizer_name
        )
        return data_transformation_config
