from src.cnnClassifier.components.prepare_callbacks import prepareCallbacks
from src.cnnClassifier.components.training import Training 
from src.cnnClassifier import logger
from src.cnnClassifier.config.configuration import ConfigManager  

STAGE_NAME = "Training Stage" 

class ModelTrainingPipeline: 
    def __init__(self):
        pass 

    def main(self): 
        config = ConfigManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()

        prepare_callbacks = prepareCallbacks(config=prepare_callbacks_config)
        callbacks_list = prepare_callbacks.get_callbacks

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callbacks_list=callbacks_list)

if __name__ == "__main__":
    try: 
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e