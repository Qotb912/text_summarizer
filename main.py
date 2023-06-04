from text_summarizer.logging import logger
from text_summarizer.pipeline.v_0_stage_0_1_data_ingestion import DataIngestionTrainingPipeline

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