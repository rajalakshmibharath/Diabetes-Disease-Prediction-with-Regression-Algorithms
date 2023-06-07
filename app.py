#include all the modules in requirements.txt
from flask import Flask,request,render_template
import numpy as np
import pandas as pd


from sklearn.preprocessing import StandardScaler

#importing predict_pipeline
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)
app = application

## Route for a home page
@app.route('/')
def index():
    return render_template('home.html') 

@app.route('/predict_datapoint',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('index.html')
    else:
		#reading all the input variables
        #CustomData function called from predict_pipeline
        data = CustomData(
            Pregnancies = request.form.get('Pregnancies'),
            Glucose = request.form.get('Glucose'),
            BloodPressure = request.form.get('BloodPressure'),
            SkinThickness = request.form.get('SkinThickness'),
            Insulin = request.form.get('Insulin'),
            BMI = float(request.form.get('BMI')),
            DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction')),
            Age = request.form.get('Age'))
        

		#converting data as df
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('index.html',results=int(results[0])) #the result will be in a list form so using [0]
    

if __name__=="__main__":
    app.run(host="0.0.0.0") #this host address is going to map with 127.0.0.1. usual thing