# data sources

There are three json data sources from the Fronius datalogger:

1. Realtime API
2. Archive Data (dailysum) API
2. Archive Data (detailed) API
3. Push Data



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
