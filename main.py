from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationPipeline

STAGE_NAME = "Data Ingestion Stage"

try : 
    logger.info(f"Stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(F"Stage {STAGE_NAME} COMPLETED")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try : 
    logger.info(f"Stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataTransformationPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info(F"Stage {STAGE_NAME} COMPLETED")
except Exception as e:
    logger.exception(e)
    raise e