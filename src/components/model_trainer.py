import sys
import os

from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import GridSearchCV

from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from src.utils import save_object
from src.utils import evaluate_models

@dataclass
class ModelTrainerConfig:
 #a new pkl file called preprocessor is created within artifacts which has input for thedata trasnformation
	trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
	def __init__(self):
		#this data_transformation_config will have preprocess_obj_file_path variab;e
		self.model_trainer_config = ModelTrainerConfig()

	def initiate_model_trainer(self,train_array,test_array):
		try:

			logging.info('split train and test input data : x and y')

			''' in the data trasnformation, train and test array is return
				which had the dependent and the independent feature arrays
				 (target column array)'''

			x_train,y_train,x_test,y_test = (
												train_array[:,:-1],
						                        train_array[:,-1],
			                                    test_array[:,:-1],
						                        test_array[:,-1]   )

			#Defining all models as a dictionary 

			models = {
									'LogisticRegression':LogisticRegression(),
									'DecisionTreeClassifier': DecisionTreeClassifier(),
									'KNeighborsClassifier':KNeighborsClassifier(),
									'RandomForestClassifier': RandomForestClassifier(),
									'XGBClassifier': XGBClassifier(),
									
									}

			

			#evaluate_model function is created inside utils 
			model_report:dict = evaluate_models(x_train = x_train,
											y_train = y_train,
						                    x_test = x_test,
			                                y_test = y_test,
		                                    models = models)

			
			best_model_score = max(sorted(model_report.values()))

			best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
			best_model= models[best_model_name]

			if best_model_score<0.6:
				raise CustomException('No best model found')

			logging.info('Best model found')

			save_object(file_path = self.model_trainer_config. trained_model_file_path, obj =best_model )

			predicted= best_model.predict(x_test)
			
			pred_accuracy_score = accuracy_score(y_test,predicted)
			return pred_accuracy_score


		except Exception as e:
			raise CustomException(e, sys)