from flask import request, render_template, make_response, url_for, jsonify
from flask_restful import Resource
from flask_cors import cross_origin
from ..functions.validation import validate_transaction_payload, transform
from datetime import datetime
import pandas as pd
import pickle
import numpy as np
import os
import joblib



model=None

def load_model():
    global model
    model_path = os.path.join(os.getcwd(), './api/models/', 'LightGBM_optimized.pkl')
    # model = pickle.load(open(model_path, "rb"))
    model = joblib.load(model_path)
    
load_model()
model_keys = ['transaction_amount', 'transaction_type', 'device_type', 'location', 'time_of_day', 'day_of_week',
 'is_foreign_transaction', 'is_high_risk_country', 'previous_fraud_flag', 'risk_score']


def extract_hour(timestamp):
    """
    Handles both formats by replacing 'T' with space first
    """
    normalized = timestamp.replace('T', ' ')
    return int(normalized.split(' ')[1][:2])

class FraudDetection(Resource):
    
    '''
    
    '''
    
    @classmethod
    def get(cls):
        payload = request.get_json() if request.get_json() else dict(request.form)
        print(payload)
        validation_result = validate_transaction_payload(payload)
        if validation_result:
            return validation_result, 400
        
        tran_hr = extract_hour(payload['transaction_time'])
            
        final_data = {k:v for k,v in payload.items() if k in model_keys}
        print(final_data)
        final_data['hour'] = tran_hr

        # Create new mapped dictionary
        final_payload = transform(final_data)
        print('transform data', final_payload)
        data = pd.DataFrame([final_payload])
        print(data)
        try:
            
            print('loaded the model')
            y_pred = model.predict(data)
            
            prediction = y_pred[0]
            result_proba = model.predict_proba(data)[0][1]
            if isinstance(prediction, np.floating):
                result_proba = float(result_proba)
            # Convert NumPy types to native Python
            if isinstance(prediction, np.integer):
                prediction = int(prediction)
            elif isinstance(prediction, np.floating):
                prediction = float(prediction)
            if prediction == 1 or 1.0:
                explanation = "Fraud detected: this transaction should be flagged and escalated for investigation."
            else:
                explanation = 'Not a fradulent transaction'
                
            return jsonify({
                'Status': 'Successful',
                'prediction': prediction,
                'probability': result_proba,
                'explanation': explanation})
            
            
            #return jsonify(prediction), 200
        except Exception as e:
            result = 'Invalid Prediction due to the error: {}'.format(e)
            response = {
                'Status': 'Failed',
                'Prediction': result
            }
            return response, 400


class Fraud_web(Resource):
    
    '''
    
    '''
    
    @classmethod
    def get(cls):
        payload = request.args.to_dict()  
        print(payload)
        
        tran_hr = extract_hour(payload['transaction_time'])
        
        final_data = {k:v for k,v in payload.items() if k in model_keys}
        print(final_data)
        final_data['hour'] = tran_hr
        
        # Create new mapped dictionary
        final_payload = transform(final_data)
        print('transform data', final_payload)
        data = pd.DataFrame([final_payload])
        try:
            print('loaded the model')
            y_pred = model.predict(data)
            
            prediction = y_pred[0]
            result_proba = model.predict_proba(data)[0][1]
            if isinstance(prediction, np.floating):
                result_proba = float(result_proba)
            # Convert NumPy types to native Python
            if isinstance(prediction, np.integer):
                prediction = int(prediction)
            elif isinstance(prediction, np.floating):
                prediction = float(prediction)
            if prediction == 1 or 1.0:
                explanation = "Fraud detected: this transaction should be flagged and escalated for investigation."
            else:
                explanation = 'Not a fradulent transaction'
                
            predicted_data = jsonify({
                'Status': 'Successful',
                'prediction': prediction,
                'probability': result_proba,
                'explanation': explanation})
            
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('index.html', response = predicted_data.json), headers)
            
            #return jsonify(prediction), 200
        except Exception as e:
            result = 'Invalid Prediction due to the error: {}'.format(e)
            response = {
                'Status': 'Failed',
                'Prediction': result,
                'explanation': 'An error occured'
            }
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('index.html', response = response), headers)
