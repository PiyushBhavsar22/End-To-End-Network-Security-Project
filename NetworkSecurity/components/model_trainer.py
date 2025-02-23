import os
import sys

from NetworkSecurity.exception.exception import NetworkSecurityException 
from NetworkSecurity.logging.logger import logging

from NetworkSecurity.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from NetworkSecurity.entity.config_entity import ModelTrainerConfig



from NetworkSecurity.utils.ml_utils.model.estimator import NetworkModel
from NetworkSecurity.utils.main_utils.utils import save_object,load_object
from NetworkSecurity.utils.main_utils.utils import load_numpy_array_data,evaluate_models
from NetworkSecurity.utils.ml_utils.metric.classification_metric import get_classification_score

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
import mlflow
from urllib.parse import urlparse

import dagshub