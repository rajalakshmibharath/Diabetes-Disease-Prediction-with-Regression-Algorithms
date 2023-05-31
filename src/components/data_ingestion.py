import os 
import sys #will be using exception
from src.exception import CustomException #importing exception handling that we created
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass #it is used to create dat variables

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


#the below class shows that components where to save thetrain data , test data ans he raw data 
@dataclass  #basically inside a class to define variuables we used init function but wecan directly assign variable if we use dataclass decorator
class DataIngestionConfig: #is used to store the input realatedto data ingestion
	train_data_path:str = os.path.join('artifacts','train.csv')
	test_data_path:str = os.path.join('artifacts','test.csv')
	raw_data_path:str = os.path.join('artifacts','data.csv')

#* When we are onl;y defining variables we can use dataclas but we have some functionalities we use inint function
class DataIngestion:
	def __init__(self):
		self.ingestion_config = DataIngestionConfig()  # initalizing the ingestion config clas and storing insiide the variable 
			
	def initiate_data_ingestion(self):
		logging.info('Entered the data ingestion method')

		try:
			df = pd.read_csv('notebook\data\diabetes.csv')
			logging.info('Read the dataset from csv file')

			os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)

			df.to_csv(self.ingestion_config.raw_data_path, index= False, header= True)

			logging.info('Train test split initiated')
			train_set,test_set = train_test_split(df, test_size= 0.2, random_state = 42 )

			train_set.to_csv(self.ingestion_config.train_data_path, index= False, header= True)	
			test_set.to_csv(self.ingestion_config.test_data_path, index= False, header= True)	

			logging.info('Data ingestion completed')

			return(self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)


		except Exception as e:
			raise CustomException(e,sys)

if __name__=='__main__':
		obj = DataIngestion()
		train_data,test_data= obj.initiate_data_ingestion()

		data_transformation_obj = DataTransformation()
		train_arr,test_arr,_= data_transformation_obj.initiate_data_transformation(train_data,test_data)