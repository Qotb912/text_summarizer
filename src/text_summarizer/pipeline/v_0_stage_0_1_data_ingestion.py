
from text_summarizer.config.configration import ConfigurationManager
from text_summarizer.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self): 
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_inngestion = DataIngestion(config=data_ingestion_config)
        data_inngestion.download_file()
        data_inngestion.etract_zip_file()