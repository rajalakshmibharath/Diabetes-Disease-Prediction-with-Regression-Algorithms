import sys
import os
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE


from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

from src.utils import replace_func
from src.utils import save_object


#this defines the input path required for the data transformation (here the input for the transformation will be saved)
@dataclass
class DataTransformationConfig:
 #a new pkl file called preprocessor is created within artifacts which has input for thedata trasnformation
	preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')




class DataTransformation:
	def __init__(self):
		#this data_transformation_config will have preprocess_obj_file_path variab;e
		self.data_transformation_config = DataTransformationConfig()

	def get_data_transformer_obj(self):
		try:
			all_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

			num_pipeline = Pipeline(steps=[
				('replace',FunctionTransformer(replace_func)),
				('imputer', SimpleImputer(strategy='median')),
				('scalar', StandardScaler())
			])

			logging.info('Categorical and numerical features transformation done')

			# using ColumnTransformer to combine these preprocessing steps
			preprocessor = ColumnTransformer(transformers=[('num_pipeline', num_pipeline, all_columns)])

			return preprocessor

		except Exception as e:
			raise CustomException(e, sys)


	def initiate_data_transformation(self, train_path, test_path):
		try:
			train_df = pd.read_csv(train_path)
			test_df = pd.read_csv(test_path)

			logging.info('Train and test data is read')

			logging.info('Obtaining preprocessing object')

			preprocessing_obj = self.get_data_transformer_obj()

			target_column_name = 'Outcome'
			all_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

			input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
			target_feature_train_df = train_df[target_column_name]

			input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
			target_feature_test_df = test_df[target_column_name]

			logging.info('Applying preprocessing techniques to train and test dataset')

			input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
			input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

			#sm = SMOTE()
			#input_feature_train_arr,target_feature_train_df = sm.fit_resample(input_feature_train_arr,target_feature_train_df)

			# Print shapes for debugging
			#print("Shape of input_feature_train_arr:", input_feature_train_arr.shape)
			#print("Shape of input_feature_test_arr:", input_feature_test_arr.shape)
			#print("Number of columns in input_feature_train_df:", input_feature_train_df.shape[1])
			#print(len(all_columns))
			#print("Number of transformers in preprocessor:", len(preprocessing_obj.transformers_))

			# converting the features both input and target to numpy array
			train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
			test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

			logging.info('Saved preprocessing object')

			# saving all the preprocessing object data in a pickle file inside artifacts
			save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
						obj=preprocessing_obj)

			return train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path

		except Exception as e:
			raise CustomException(e, sys)


