from flask import Flask, request
import requests
import numpy as np

app = Flask(__name__)

@app.route('/api',methods=['GET','POST'])
def get_forecast():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    # set headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    response = requests.get(f'https://api.safecast.org/measurements.json?latitude={lat}&longitude={lon}', headers=headers)
    response.raise_for_status
    # access JSON content
    jsonResponse = response.json()

    # iterate through captures
    valueArray = []
    for i in range(len(jsonResponse)):
        # take values from response
        respUnit = jsonResponse[i]['unit']
        respValue = jsonResponse[i]['value']
        
        valueArray.append(respValue)

    # calculate mean value
    meanVal = np.mean(valueArray)
    return {'Latitude': lat,
            'Longitude': lon,
            'Unit': respUnit,
            'Value': meanVal}

# error handling
@app.errorhandler(Exception)
def resource_not_found(e):
    return {'Error': str(e)}