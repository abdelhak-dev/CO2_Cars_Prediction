import streamlit as stream
import pandas as pd
import numpy as np
import reg_emiCO2
import features
#=======================
stream.set_page_config(
    page_title="CO2 Assistance",
    page_icon="⚙",
)
#


stream.title('Demo: CO2 Assistance')
stream.markdown('Toy model to play to estimate the CO2 Amount  \
based on Car weight  and Volume ')

stream.header("Estimation CO2")

Car_Weight = stream.slider("Car_Weight (Kg)", 0.0, 1600.0)
Car_Volume = stream.slider("Car_Volume (mm^3)", 1.0, 2500.0)
Co2_Value = features.AskModel(Car_Volume, Car_Weight)
stream.write("The CO2 Amount is ", Co2_Value, '(grams/Kg)')