from src.cnnClassifier.constants import * 
from src.cnnClassifier.utils.common import read_yaml, create_directories 
from src.cnnClassifier.entity.config_entity import (DataIngestionConfig,PrepareBaseModelConfig,PrepareCallbacksConfig,TrainingConfig,EvaluationConfig)
import os
from pathlib import Path

class ConfigManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
        return data_ingestion_config 
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model 

        create_directories([config.root_dir])  
        
        prepare_base_model_config_obj = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.params_image_size,
            params_learning_rate=self.params.params_learning_rate,
            params_weights=self.params.params_weights,
            params_classes=self.params.params_classes,
            params_include_top=self.params.params_include_top
        )
        return prepare_base_model_config_obj
    
    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories(
            [
                Path(config.tensorboard_log_dir),
                Path(model_ckpt_dir)
            ])
        prepare_callbacks_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_log_dir=Path(config.tensorboard_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )
        return prepare_callbacks_config 
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data_path =os.path.join(self.config.data_ingestion.unzip_dir,"Chicken fickle images")
        create_directories([Path(training.root_dir)])
        
        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data_path),
            params_epoch=params.params_epoch,
            params_batch_size=params.params_batch_size,
            params_is_augmentation=params.params_is_augmentation,
            params_image_size=params.params_image_size
        )
        return training_config
         
    def get_evaluation_config(self) -> EvaluationConfig:
        evaluation_config = EvaluationConfig(
            path_of_model=Path("artifacts/training/model.h5"),
            all_params=self.params,
            train_data_path=Path("artifacts/data_ingestion/Chicken fickle images"),
            param_batch_size=self.params.params_batch_size,
            param_image_size=self.params.params_image_size
        )
        return evaluation_config
        