import tensorflow as tf 
from pathlib import Path 
from src.cnnClassifier.entity.config_entity import EvaluationConfig 
from src.cnnClassifier.utils.common import save_json 

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
          
    def _valid_generator(self):
        datagen_kwargs = dict(rescale=1./255,validation_split=0.30) 
        dataflow_kwargs = dict(
            target_size=self.config.param_image_size[:-1],
            batch_size=self.config.param_batch_size,
            interpolation="bilinear"
        )

        valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs) 

        self.valid_generator = valid_datagen.flow_from_directory(
            directory=self.config.train_data_path, 
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def _load_model(path_of_model: Path)-> tf.keras.Model:
        model = tf.keras.models.load_model(path_of_model)
        return model 

    def evaluate_model(self):
        self.model = self._load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator) 

    def save_score(self): 
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path = Path("scores.json"),data =  scores)