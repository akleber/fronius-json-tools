# fronius-json-tools
Python tools to work with the json data of the Fronius Solar API.

These are miscellaneous scripts I wrote while working with the Solar API.
They mostly lack documentation right now and are sometimes incomplete.
Nevertheless my goal is to continously work on them until they fit my needs.

# Goals
* Understand and document the Solar API
* Python cron script that fetches all available live data of the datalogger and saves it into a sqlite db
* Python script that import the datalogger archive data into the sqlite db
* Generate relevant graphs from db
* iOS app and today widget that shows live data from datalogger

# TODOs
* document setup/getting started

# Relevant Graphs
* Battery Charge throughout the day
* Overview
  * P_Load (area)
  * P_Grid (line)
  * P (line)
  * SOC (line)

# API Links
* <http://fronius/solar_api/v1/GetActiveDeviceInfo.cgi?DeviceClass=System>
* <http://fronius/solar_api/v1/GetInverterInfo.cgi>
* <http://fronius/solar_api/v1/GetInverterRealtimeData.cgi?Scope=System>
* <http://fronius/solar_api/v1/GetLoggerInfo.cgi>
* <http://fronius/solar_api/v1/GetLoggerLEDInfo.cgi>
* <http://fronius/solar_api/v1/GetMeterRealtimeData.cgi?Scope=System>
* <http://fronius/solar_api/v1/GetPowerFlowRealtimeData.fcgi>
* <http://fronius/solar_api/v1/GetStorageRealtimeData.cgi?Scope=System>
* <http://fronius/solar_api/v1/GetArchiveData.cgi?Scope=System&StartDate=1.11.2016&EndDate=11.11.2016&SeriesType=DailySum&Channel=EnergyReal_WAC_Sum_Produced&Channel=InverterErrors>
* <http://fronius/solar_api/v1/GetArchiveData.cgi?Scope=System&StartDate=1.11.2016&EndDate=1.11.2016&Channel=EnergyReal_WAC_Sum_Produced&Channel=EnergyReal_WAC_Minus_Absolute>

# Notes on Data
* ActiveDeviceInfo: Dependent on the hardware, should never change
* InverterInfo: Mostly dependend on Hardware, Configuration, should seldome change, except status and error code
* InverterRealtimeData: All data also available from PowerFlowRealtimeData.
  * PAC = abs(P_Load + P_Grid)
* LoggerInfo: Mostly dependend on Hardware, Configuration, should seldom change
* LoggerLEDInfo: Some minor status infos, should seldom change
* MeterRealimeData: Interesting Data is here
* PowerFlowRealtimeData: Summary of most important data. Faster then all other endpoints (fcgi)
  * If Inverter is in Standby P_Akku and P_PV is "null", if only the Battery is in Standby but the Inverter is providing
    PV power then P_Akku is "0"
* StorageRealtimeData: Interesting stuff about the battery

# Notes on GetArchivData
* Query interval is restricted to 16 days
* SeriesType=DailySum sums up all saved (144 per day) Values, if it makes sense or not. For example the EnergyReal_WAC_Plus_Absolute value from the meter is the absolute value every 5 minutes, and suming up this value does not make sense.
* The channel TimeSpanInSec shows the "exact" time span between two time points, typically between 298 and 306
* The Channel Temperature_Powerstage is not available on my Fronius Symo Hybrid 3.0-3-S
* GetArchivData is quite slow

#API Changes

1.2.3-1 -> 1.3.2-3
* GetActiveDeviceInfo.json
  * Body.Data.Ohmpilot added
* GetMeterRealtimeData.json
  * Body.Data.0.Details.Model: "Fronius Smart Meter 63A" change to "Smart Meter 63A"
  * Body.Data.0.PowerApparent_S_Phase_1 added
  * Body.Data.0.PowerApparent_S_Phase_2 added
  * Body.Data.0.PowerApparent_S_Phase_3 added
* GetPowerFlowRealtimeData.json
  * Body.Data.Inverters.1.E_Day added
  * Body.Data.Inverters.1.E_Total added
  * Body.Data.Inverters.1.E_Year added
  * Body.Data.Site.rel_Autonomy added
  * Body.Data.Site.rel_SelfConsumption added
* GetStorageRealtimeData.json
  * Body.Data.0.Controller.DesignedCapacity removed
    * also in Body.Data.0.Modules removed
  * Body.Data.0.Controller.Capacity_Maximum added
    * also in Body.Data.0.Modules removed

1.3.2-3 -> 1.4.1-11
* GetInverterRealtimeData.json
  * Head.RequestArguments.DataCollection removed
* GetPowerFlowRealtimeData.json
  * Body.Data.Site.BatteryStandby added
* GetStorageRealtimeData.json
  * Body.Data.0.Controller.Details.Menufacturer: "Sony" changed to "Fronius International"
  * Body.Data.0.Controller.Details.Model: "C5" changed to "Fronius Solar Battery"
* Float values now have a lot more digits

