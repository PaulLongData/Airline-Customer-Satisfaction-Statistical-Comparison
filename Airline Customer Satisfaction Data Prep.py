# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 12:26:21 2023

@author: pauly
"""

import pandas as pd
import numpy as np


TWAData = pd.read_csv(
    "C:/Users/pauly/Documents/Pre Two Way ANOVA Data.csv"
    )

TWAData['Total'] = (TWAData['inflight_wifi_service']+
                    TWAData['departure_arrival_time_convenient']+
                    TWAData['ease_of_online_booking']+TWAData['checkin_service']+
                    TWAData['gate_location']+TWAData['food_and_drink']+
                    TWAData['online_boarding']+TWAData['seat_comfort']+
                    TWAData['inflight_entertainment']+TWAData['onboard_service']+
                    TWAData['leg_room_service']+TWAData['baggage_handling']+
                    TWAData['inflight_service']+TWAData['cleanliness'])/14

TWAData = TWAData.drop(columns = ['customer_type', 'Gender', 'type_of_travel', 
                                  'inflight_wifi_service', 'cleanliness',
                                  'departure_arrival_time_convenient',
                                  'ease_of_online_booking','gate_location',
                                  'food_and_drink','online_boarding',
                                  'seat_comfort','inflight_entertainment',
                                  'onboard_service','leg_room_service',
                                  'baggage_handling','inflight_service', 
                                  'checkin_service', 'flight_distance',
                                  'Unnamed: 0', 'age', 'satisfaction'])
TWAData['Punctuality'] = 'Slight Late'

for i in range (0, len(TWAData)):
    if TWAData['arrival_delay_in_minutes'][i]+TWAData['departure_delay_in_minutes'][i] < 30:
        TWAData['Punctuality'][i] = 'On Time'
    if TWAData['arrival_delay_in_minutes'][i]+TWAData['departure_delay_in_minutes'][i] >= 60:
        TWAData['Punctuality'][i] = 'Late'
    if TWAData['arrival_delay_in_minutes'][i]+TWAData['departure_delay_in_minutes'][i] >= 120:
        TWAData['Punctuality'][i] = 'Very Late'
    
    
TWAData = TWAData.sort_values(['customer_class', 'Punctuality'],ascending = [True, True])

TWAData = TWAData.drop(columns = ['departure_delay_in_minutes', 'arrival_delay_in_minutes'])
TWAData.rename(columns = {'customer_class':'Class'}, inplace = True) 
TWAData = TWAData.reindex(columns=['Class', 'Punctuality', 'Total'])

for i in range (0, len(TWAData)):
    if TWAData['Class'][i]== 'Eco Plus':
        TWAData['Class'][i] = 'Eco'

del i

TWADataEOT = TWAData.loc[TWAData['Class'] == 'Eco']
TWADataEOT = TWADataEOT.loc[TWADataEOT['Punctuality'] == 'On Time']
TWADataEOT = TWADataEOT.sample(n=1500,replace=False)
TWADataEOT = TWADataEOT.reset_index()

TWADataBOT = TWAData.loc[TWAData['Class'] == 'Business']
TWADataBOT = TWADataBOT.loc[TWADataBOT['Punctuality'] == 'On Time']
TWADataBOT = TWADataBOT.sample(n=1500,replace=False)
TWADataBOT = TWADataBOT.reset_index()

TWADataESL = TWAData.loc[TWAData['Class'] == 'Eco']
TWADataESL = TWADataESL.loc[TWADataESL['Punctuality'] == 'Slight Late']
TWADataESL = TWADataESL.sample(n=1500,replace=False)
TWADataESL = TWADataESL.reset_index()

TWADataBSL = TWAData.loc[TWAData['Class'] == 'Business']
TWADataBSL = TWADataBSL.loc[TWADataBSL['Punctuality'] == 'Slight Late']
TWADataBSL = TWADataBSL.sample(n=1500,replace=False)
TWADataBSL = TWADataBSL.reset_index()

TWADataEL = TWAData.loc[TWAData['Class'] == 'Eco']
TWADataEL = TWADataEL.loc[TWADataEL['Punctuality'] == 'Late']
TWADataEL = TWADataEL.sample(n=1500,replace=False)
TWADataEL = TWADataEL.reset_index()

TWADataBL = TWAData.loc[TWAData['Class'] == 'Business']
TWADataBL = TWADataBL.loc[TWADataBL['Punctuality'] == 'Late']
TWADataBL = TWADataBL.sample(n=1500,replace=False)
TWADataBL = TWADataBL.reset_index()

TWADataEVL = TWAData.loc[TWAData['Class'] == 'Eco']
TWADataEVL = TWADataEVL.loc[TWADataEVL['Punctuality'] == 'Very Late']
TWADataEVL = TWADataEVL.sample(n=1500,replace=False)
TWADataEVL = TWADataEVL.reset_index()

TWADataBVL = TWAData.loc[TWAData['Class'] == 'Business']
TWADataBVL = TWADataBVL.loc[TWADataBVL['Punctuality'] == 'Very Late']
TWADataBVL = TWADataBVL.sample(n=1500,replace=False)
TWADataBVL = TWADataBVL.reset_index()

TWAData = pd.concat([TWADataEOT, TWADataBOT, TWADataESL, TWADataBSL,
                     TWADataEL, TWADataBL, TWADataEVL, TWADataBVL])
TWAData = TWAData.reset_index()

del TWADataBL
del TWADataBOT
del TWADataBSL
del TWADataBVL
del TWADataEL
del TWADataEOT
del TWADataESL
del TWADataEVL

TWAData = TWAData.drop(columns = ['level_0', 'index'])

#TWAData.to_csv('TWA Data Sample.csv', index=False)

