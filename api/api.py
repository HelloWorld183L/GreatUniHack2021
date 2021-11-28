from flask import Flask, request
import requests, time
import numpy as np
from sevlevels import levels

app = Flask(__name__)

@app.route('/api',methods=['GET','POST'])
def get_forecast():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    # set headers
    headers = {
        'mode': 'cors',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    response = requests.get(f'https://api.safecast.org/measurements.json?latitude={lat}&longitude={lon}&unit=cpm', headers=headers)
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

    # match severity
    if (meanVal >= 0) & (meanVal < 12):
        respLabel = "low"
    elif (meanVal >= 12) & (meanVal < 25):              #############################################
        respLabel = "average"                           # i was planning on using a switch-case for #
    elif (meanVal >= 25) & (meanVal < 50):              # this, but it turns out a bunch of if/else #
        respLabel = "slightly_above_average"            # statements is actually more efficient and #
    elif (meanVal >= 50) & (meanVal < 60):              #          better for performance           #
        respLabel = "above_average"                     #############################################
    elif (meanVal >= 60) & (meanVal < 100):                   # <============================ #
        respLabel = "high"                                     ###############################
    elif (meanVal >= 100) & (meanVal < 150):
        respLabel = "very_high"
    elif (meanVal >= 150) & (meanVal < 500):
        respLabel = "extremely_high"
    elif (meanVal >= 500) & (meanVal < 50000):
        respLabel = "disaster"

    # create JSON object
    respObject = {'current_value': meanVal,
                  'unit': respUnit,
                  'current_date': time.strftime('%Y-%m-%d'),
                  'current_report': {'report_type': 'current',
                                     'radiation_label': respLabel,
                                     'min_value': levels[respLabel]['min_value'],
                                     'max_value': levels[respLabel]['max_value'],
                                     'description': levels[respLabel]['description'],
                                     'advice': levels[respLabel]['advice']}}

    # return JSON object
    return respObject

# error handling
@app.errorhandler(Exception)
def resource_not_found(e):
    return {'Error': str(e)}