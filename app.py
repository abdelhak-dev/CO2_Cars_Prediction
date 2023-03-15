from fastapi import FastAPI
import reg_emiCO2
from fastapi import FastAPI, HTTPException
from features import *
from typing import Optional
import datetime
import json
from sklearn import datasets, linear_model
from sklearn.metrics import accuracy_score,mean_squared_error
import joblib


tags_metadata = [
    {
        "name": "Welcome:",
        "description": "Welcome ! ENjoy the work ✌",
    },
    {
        "name": "Get Predictions :",
        "description": "Cars CO2 emission Prediction, insert Data to predict for ex: weight and Car Volume",
    },

    {
        "name": "Get Response:",
        "description": "Get response from API about:volume and weight.",
        "externalDocs": {
            #"description": "The local API URL's ",
            "url": "http://127.0.0.3:8000/",
        },
    },

]

app = FastAPI(title="CO2 Assistance",version="1.5.0",description=" ✌️" ,openapi_tags=tags_metadata)


'''
Le fichier app contient les URI API pour les différentes requetes utiles pour notre projet CO2 Assistance.

'''


# message d'entée de l'api
@app.get("/", tags=['Welcome'])
async def root():
    return {"Project": " Welcome to The CO2 Assistant ! To acces add '/docs' query after API URL"}


### get_functions tag:
##
#

# Créer une route dans l'api qui renvoi une réponse selon les différents caractéristiques
# exemple: verbe/{argument1}/{arguemnt2}

#Faire une prédiction selon les valeurs des caractèrestiques
@app.get('/PredictCO2/{Car_Volume}/{Car_Weight}',tags=["Get Predictions"])
async def PredictCO2(Car_Volume:int,Car_Weight:int):
    print("code:200 Done !")
    return AskModel(Car_Volume,Car_Weight)

