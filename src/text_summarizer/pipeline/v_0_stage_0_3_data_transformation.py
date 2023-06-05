from text_summarizer.components.data_transformation import DataTransformation
from text_summarizer.config.configration import ConfigurationManager


class DataTransormationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
       try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
       except Exception as e:
           raise e