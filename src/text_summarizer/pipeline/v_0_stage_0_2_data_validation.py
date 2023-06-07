
from text_summarizer.components.data_validation import DataValidation
from text_summarizer.config.configration import ConfigurationManager


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        print(config)
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
        