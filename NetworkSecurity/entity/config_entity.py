from datetime import datetime
import os
from NetworkSecurity.constant import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):


class DataIngestionConfig:
    def __init__(self,training_pipeline_config):
        pass