import os 
import urllib.request as request
import zipfile
import tensorflow as tf
import time 
from src.cnnClassifier.entity.config_entity import PrepareCallbacksConfig

class prepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tensorboard_callback(self):
        tensorboard_log_dir = os.path.join(
            self.config.tensorboard_log_dir,
            f"tb_logs_at_{time.strftime('%Y-%m-%d-%H-%M-%S')}"
        )
        tensorboard_callback = tf.keras.callbacks.TensorBoard(
            log_dir=tensorboard_log_dir
        )
        return tensorboard_callback 
     
    @property
    def _create_model_checkpoint_callback(self):
        model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
        return model_checkpoint_callback
         
    @property
    def get_callbacks(self):
        return [
            self._create_tensorboard_callback,
            self._create_model_checkpoint_callback
        ]