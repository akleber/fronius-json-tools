
"""
This script expects three parameters: start_date, end_date, and subdir.
Example:
python3 archivedata2json.py 01.01.2016 30.01.2016 my_archive_data

It then uses the GetArchiveData API to obtain the saved data and writes it to 
one json file per day. It fetches the detailed data per day as well as 
the daily sum values per day.
"""

import requests
import sys
import os
import json
import time
from datetime import timedelta, date, datetime

hostname = "fronius"

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days + 1)):
        yield start_date + timedelta(n)

def main(argv):
    subdir = argv[3]

    if not os.path.exists(subdir):
        os.makedirs(subdir)

    #start_date = date(2016, 11, 1)
    #end_date = date(2016, 11, 1)

    start_date = datetime.strptime(argv[1], "%d.%m.%Y")
    end_date = datetime.strptime(argv[2], "%d.%m.%Y")

    print("Start data: " + start_date.strftime("%d.%m.%Y"))
    print("End date " + end_date.strftime("%d.%m.%Y"))
    print("Subdir: " + subdir)

    for single_date in daterange(start_date, end_date):
        datestring = single_date.strftime("%d.%m.%Y")
        datestring_reversed = single_date.strftime("%Y-%m-%d")
        print("Daily Sum for: " + datestring)

        url = "http://" + hostname + "/solar_api/v1/GetArchiveData.cgi?Scope=System&StartDate=" + \
            datestring + "&EndDate=" + datestring + "&SeriesType=DailySum&Channel=EnergyReal_WAC_Sum_Produced&Channel=InverterErrors"

        r = requests.get(url, timeout=120)
        r.raise_for_status()
        jsondata = r.json()

        with open(os.path.join(subdir, "archivedata_dailysum_" + datestring_reversed + ".json"), 'w') as f:
            json.dump(jsondata, f, indent=4)


        print("Day : " + datestring)
        url = "http://" + hostname + "/solar_api/v1/GetArchiveData.cgi?Scope=System&StartDate=" + \
            datestring + "&EndDate=" + datestring + "&Channel=EnergyReal_WAC_Plus_Absolute&Channel=EnergyReal_WAC_Minus_Absolute"

        r = requests.get(url, timeout=120)
        r.raise_for_status()
        jsondata = r.json()

        with open(os.path.join(subdir, "archivedata_day_" + datestring_reversed + ".json"), 'w') as f:
            json.dump(jsondata, f, indent=4)

        print("Finished day: " + datestring)
        time.sleep(3)

if __name__ == "__main__":
    main(sys.argv)

