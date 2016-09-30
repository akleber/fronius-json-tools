import urllib
import json
import time
import collections

hostname = "192.168.134.104"

data = collections.OrderedDict()

# Powerflow
starttime = time.time()

powerflow_url = "http://" + hostname + "/solar_api/v1/GetPowerFlowRealtimeData.fcgi"
powerflow_response = urllib.urlopen(powerflow_url)
powerflow_data = json.loads(powerflow_response.read())

data['powerflow_timestamp'] = powerflow_data['Head']['Timestamp']
data['powerflow_mode'] = powerflow_data['Body']['Data']['Site']['Mode']
data['powerflow_P_Grid'] = powerflow_data['Body']['Data']['Site']['P_Grid']
data['powerflow_P_Load'] = powerflow_data['Body']['Data']['Site']['P_Load']
data['powerflow_P_Akku'] = powerflow_data['Body']['Data']['Site']['P_Akku']
data['powerflow_P_PV'] = powerflow_data['Body']['Data']['Site']['P_PV']
data['powerflow_E_Day'] = powerflow_data['Body']['Data']['Site']['E_Day']
data['powerflow_E_Year'] = powerflow_data['Body']['Data']['Site']['E_Year']
data['powerflow_E_Total'] = powerflow_data['Body']['Data']['Site']['E_Total']

print time.time()-starttime

# meter
starttime = time.time()

meter_url = "http://" + hostname + "/solar_api/v1/GetMeterRealtimeData.cgi?Scope=System"
meter_response = urllib.urlopen(meter_url)
meter_data = json.loads(meter_response.read())

data['meter_timestamp'] = meter_data['Head']['Timestamp']
data['meter_timestamp2'] = meter_data['Body']['Data']['0']['TimeStamp']
data['meter_PowerReal_P_Sum'] = meter_data['Body']['Data']['0']['PowerReal_P_Sum']
data['meter_PowerReal_P_Phase_1'] = meter_data['Body']['Data']['0']['PowerReal_P_Phase_1']
data['meter_PowerReal_P_Phase_2'] = meter_data['Body']['Data']['0']['PowerReal_P_Phase_2']
data['meter_PowerReal_P_Phase_3'] = meter_data['Body']['Data']['0']['PowerReal_P_Phase_3']
data['meter_PowerReactive_Q_Sum'] = meter_data['Body']['Data']['0']['PowerReactive_Q_Sum']
data['meter_PowerReactive_Q_Phase_1'] = meter_data['Body']['Data']['0']['PowerReactive_Q_Phase_1']
data['meter_PowerReactive_Q_Phase_2'] = meter_data['Body']['Data']['0']['PowerReactive_Q_Phase_2']
data['meter_PowerReactive_Q_Phase_3'] = meter_data['Body']['Data']['0']['PowerReactive_Q_Phase_3']
data['meter_Current_AC_Phase_1'] = meter_data['Body']['Data']['0']['Current_AC_Phase_1']
data['meter_Current_AC_Phase_2'] = meter_data['Body']['Data']['0']['Current_AC_Phase_2']
data['meter_Current_AC_Phase_3'] = meter_data['Body']['Data']['0']['Current_AC_Phase_3']
data['meter_Voltage_AC_Phase_1'] = meter_data['Body']['Data']['0']['Voltage_AC_Phase_1']
data['meter_Voltage_AC_Phase_2'] = meter_data['Body']['Data']['0']['Voltage_AC_Phase_2']
data['meter_Voltage_AC_Phase_3'] = meter_data['Body']['Data']['0']['Voltage_AC_Phase_3']
data['meter_Voltage_AC_PhaseToPhase_12'] = meter_data['Body']['Data']['0']['Voltage_AC_PhaseToPhase_12']
data['meter_Voltage_AC_PhaseToPhase_23'] = meter_data['Body']['Data']['0']['Voltage_AC_PhaseToPhase_23']
data['meter_Voltage_AC_PhaseToPhase_31'] = meter_data['Body']['Data']['0']['Voltage_AC_PhaseToPhase_31']
data['meter_Frequency_Phase_Average'] = meter_data['Body']['Data']['0']['Frequency_Phase_Average']
data['meter_PowerApparent_S_Sum'] = meter_data['Body']['Data']['0']['PowerApparent_S_Sum']
data['meter_PowerFactor_Sum'] = meter_data['Body']['Data']['0']['PowerFactor_Sum']
data['meter_PowerFactor_Phase_1'] = meter_data['Body']['Data']['0']['PowerFactor_Phase_1']
data['meter_PowerFactor_Phase_2'] = meter_data['Body']['Data']['0']['PowerFactor_Phase_2']
data['meter_PowerFactor_Phase_3'] = meter_data['Body']['Data']['0']['PowerFactor_Phase_3']
data['meter_EnergyReal_WAC_Sum_Produced'] = meter_data['Body']['Data']['0']['EnergyReal_WAC_Sum_Produced']
data['meter_EnergyReal_WAC_Sum_Consumed'] = meter_data['Body']['Data']['0']['EnergyReal_WAC_Sum_Consumed']
data['meter_EnergyReactive_VArAC_Sum_Produced'] = meter_data['Body']['Data']['0']['EnergyReactive_VArAC_Sum_Produced']
data['meter_EnergyReactive_VArAC_Sum_Consumed'] = meter_data['Body']['Data']['0']['EnergyReactive_VArAC_Sum_Consumed']
data['meter_EnergyReal_WAC_Plus_Absolute'] = meter_data['Body']['Data']['0']['EnergyReal_WAC_Plus_Absolute']
data['meter_EnergyReal_WAC_Minus_Absolute'] = meter_data['Body']['Data']['0']['EnergyReal_WAC_Minus_Absolute']

print time.time()-starttime

# battery
starttime = time.time()

battery_url = "http://" + hostname + "/solar_api/v1/GetStorageRealtimeData.cgi?Scope=System"
battery_response = urllib.urlopen(battery_url)
battery_data = json.loads(battery_response.read())

data['battery_controller_timestamp'] = battery_data['Head']['Timestamp']
data['battery_controller_timestamp2'] = battery_data['Body']['Data']['0']['Controller']['TimeStamp']
data['battery_controller_StateOfCharge_Relative'] = battery_data['Body']['Data']['0']['Controller']['StateOfCharge_Relative']
data['battery_controller_Voltage_DC'] = battery_data['Body']['Data']['0']['Controller']['Voltage_DC']
data['battery_controller_Current_DC'] = battery_data['Body']['Data']['0']['Controller']['Current_DC']
data['battery_controller_Temperature_Cell'] = battery_data['Body']['Data']['0']['Controller']['Temperature_Cell']
data['battery_controller_Voltage_DC_Maximum_Cell'] = battery_data['Body']['Data']['0']['Controller']['Voltage_DC_Maximum_Cell']
data['battery_controller_Voltage_DC_Minimum_Cell'] = battery_data['Body']['Data']['0']['Controller']['Voltage_DC_Minimum_Cell']

print time.time()-starttime

# Print
for key, value in data.items():
	print('{}: {}'.format(key, value))

# Save to DB

