import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object #function to load the pickle file
import os


class PredictPipeline:
    def __init__(self):
        pass
		
	#this is model prediction
    def predict(self,features):
        try:
            model_path = os.path.join("artifacts","model.pkl")
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")

			#loas_object function iscalled from utils to load the pkl files
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
						
			#Applying preprocessing steps to input data using preprocesser
            data_scaled = preprocessor.transform(features)

			#predicting using model
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


#the class helps in mapping the inputs that we give in the fromt end to thebackend
class CustomData: 
    
	#defining the datatype
    def __init__( self,
        Pregnancies: int,
        Glucose: int,
        BloodPressure: int ,
        SkinThickness: int,
        Insulin: int,
        BMI: float,
        DiabetesPedigreeFunction: float,
        Age: int):
				
		#creating variabvle using self--here the values are assigned from the fromt end ie values from the home.html mapped by the name
        self.Pregnancies = Pregnancies

        self.Glucose = Glucose

        self.BloodPressure = BloodPressure

        self.SkinThickness = SkinThickness

        self.Insulin = Insulin

        self.BMI = BMI

        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction

        self.Age = Age

	#this function returns all the input from above as a dataframe as we trained our mopdel as a dataframe
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Pregnancies": [self.Pregnancies],
                "Glucose": [self.Glucose],
                "BloodPressure": [self.BloodPressure],
                "SkinThickness": [self.SkinThickness],
                "Insulin": [self.Insulin],
                "BMI": [self.BMI],
                "DiabetesPedigreeFunction": [self.DiabetesPedigreeFunction],
                "Age": [self.Age],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)