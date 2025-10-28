import sys, os
sys.path.append(os.path.join(os.getcwd(), "src"))
from src.cnnClassifier.config.configuration import ConfigManager 
from src.cnnClassifier.components.model_evaluation import Evaluation 
from src.cnnClassifier import logger 

STAGE_NAME = "Evaluation stage" 

class EvaluationPipeline:
    def __init__(self):
        pass 

    def main(self): 
        config_manager = ConfigManager()
        evaluation_config = config_manager.get_evaluation_config()

        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluate_model()
        evaluation.save_score()  


if __name__ == "__main__": 
    try: 
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e