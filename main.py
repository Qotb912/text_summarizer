from text_summarizer.logging import logger
from text_summarizer.pipeline.v_0_stage_0_1_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.v_0_stage_0_2_data_validation import DataValidationTrainingPipeline
from text_summarizer.pipeline.v_0_stage_0_3_data_transformation import DataTransormationTrainingPipeline




VERSION = '0'


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"-------------- VERSION {VERSION}  ------------------")
    logger.info(f"-------------- STAGE {STAGE_NAME}  ------------------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"--------- VERSION {VERSION} && STAGE {STAGE_NAME} && COMPLETED  ----------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation"
try:
    logger.info(f"-------------- VERSION {VERSION}  ------------------")
    logger.info(f"-------------- STAGE {STAGE_NAME}  ------------------")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"--------- VERSION {VERSION} && STAGE {STAGE_NAME} && COMPLETED  ----------")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation"
try:
    logger.info(f"-------------- VERSION {VERSION}  ------------------")
    logger.info(f"-------------- STAGE {STAGE_NAME}  ------------------")
    data_transformation = DataTransormationTrainingPipeline()
    data_transformation.main()
    logger.info(f"--------- VERSION {VERSION} && STAGE {STAGE_NAME} && COMPLETED  ----------")
except Exception as e:
    logger.exception(e)
    raise e
