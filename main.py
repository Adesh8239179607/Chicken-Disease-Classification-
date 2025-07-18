from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline    
from cnnClassifier.pipeline.stage_02_prepare_base_model import PreparebaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed! <<<<<<\n\nx==========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e    



STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"****************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PreparebaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed! <<<<<<\n\nx==========x") 
except Exception as e:
    logger.exception(e)
    raise e  



STAGE_NAME = "Training"

try:
    logger.info(f"****************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed! <<<<<<\n\nx==========x") 
except Exception as e:
    logger.exception(e)
    raise e  


STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"****************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed! <<<<<<\n\nx==========x") 
except Exception as e:
    logger.exception(e)
    raise e
