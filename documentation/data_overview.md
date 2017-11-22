
# Data source Overview

There are four json data sources from the Fronius datalogger:

Value                                 | Realtime | Archive Data (sum) | Archive Data (detail) | Push Data
------------------------------------- | -------- | ------------------ | --------------------- | ---------
meter/location                        |          |                    |                       | X
meter/EnergyReal_WAC_Plus_Absolute    |          |                    | X                     | X
meter/EnergyReal_WAC_Minus_Absolute   |          |                    | X                     | X
inverter/EnergyReal_WAC_Sum_Produced  |          | X                  |                       | X
inverter/Voltage_DC_String_1          |          |                    |                       | X
inverter/Current_DC_String_1          |          |                    |                       | X
inverter/Voltage_DC_String_2          |          |                    |                       | X
inverter/Current_DC_String_2          |          |                    |                       | X
inverter/InverterErrors               |          | X                  |                       | 


# Archive Data API

Notes:
* Query interval is restricted to 16 days
* SeriesType=DailySum sums up all saved (144 per day) Values, if it makes sense or not. For example the EnergyReal_WAC_Plus_Absolute value from the meter is the absolute value every 5 minutes, and suming up this value does not make sense.
* The channel TimeSpanInSec shows the "exact" time span between two time points, typically between 298 and 306
* The Channel Temperature_Powerstage is not available on my Fronius Symo Hybrid 3.0-3-S
* GetArchivData is quite slow


# Realtime API


# Push Data