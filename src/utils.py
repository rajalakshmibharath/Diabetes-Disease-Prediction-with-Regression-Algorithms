import os
import sys 
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException


	
def replace_func(X):
    try:
        for col in X.columns:
            if col=='Pregnancies':
                continue
            else:
                X[col].replace(0, np.nan,inplace= True)
        return X
    except Exception as e:
        raise CustomException(e,sys)


def save_object(file_path,obj):
	try:
		dir_path = os.path.dirname(file_path)

		os.makedirs(dir_path, exist_ok = True)
		with open(file_path,'wb') as file_obj:
			dill.dump(obj,file_obj) #dill helps to create pickle file , also include dill in requiurements

	except Exception as e:
		raise CustomException(e,sys)