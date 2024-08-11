
# This code will be used to model the thermodynamics of a house. 
# The model will have the following mandatory inputs: 
# - Outside temperature
# - On and off state of the heater
# The model will have the following optional inputs:
# - On and off state of the air conditioner
# - Outside humidity 
# - On and off state of the humidifier
# - On and off state of the dehumidifier
# - Solar radiation 
# - Wind speed 
# - Rainfall
# - On and off state of the air purifier
# - On and off state of the fan
# The outputs of the model will be: 
# - Inside temperature
# - Inside humidity
# - Inside CO2 concentration

# The model will be a state-space model with online system identification.

def house_thermodynamics(outside_temperature, heater_state, air_conditioner_state, outside_humidity, humidifier_state, dehumidifier_state, solar_radiation, wind_speed, rainfall, air_purifier_state, fan_state):
    pass