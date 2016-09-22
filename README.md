# fronius-json-tools
Python tools to work with the json data of the Fronius Solar API


# Goals
* Python cron script that fetches all available live data of the datalogger and saves it into a sqlite db
* Python script that import the datalogger archive data into the sqlite db
* Generate relevant graphs from db
* iOS app and today widget that shows live data from datalogger

# Relevant Graphs
* Battery Charge throughout the day
* 


# API Links
http://192.168.134.104/solar_api/v1/GetInverterRealtimeData.cgi?Scope=System
http://192.168.134.104/solar_api/v1/GetLoggerInfo.cgi
http://192.168.134.104/solar_api/v1/GetLoggerLEDInfo.cgi
http://192.168.134.104/solar_api/v1/GetInverterInfo.cgi
http://192.168.134.104/solar_api/v1/GetActiveDeviceInfo.cgi?DeviceClass=System
http://192.168.134.104/solar_api/v1/GetMeterRealtimeData.cgi?Scope=System
http://192.168.134.104/solar_api/v1/GetStorageRealtimeData.cgi?Scope=System
http://192.168.134.104/solar_api/v1/GetPowerFlowRealtimeData.fcgi