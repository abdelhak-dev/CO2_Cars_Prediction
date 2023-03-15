from reg_emiCO2 import load_Model,predict
from sklearn import datasets, linear_model
from sklearn.metrics import accuracy_score,mean_squared_error
import joblib
#
##
### Fonction qui renvoie la sortie de la fonction predict() sortie en fonction des caractèristiques
def AskModel(Car_Volume:int,Car_Weight:int):
    return predict(Car_Volume,Car_Weight)
