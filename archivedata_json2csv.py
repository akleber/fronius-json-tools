
"""
Converts archivedata json files gathered with archivedata2json.py
to a csv file.

Usage: archivedata2csv.py <subdir_with_json_files>
"""

import json
import csv
import os
import sys
from dateutil.parser import parse

def main(argv):
    subdir = argv[1]

    filenames = []
    for (_dirpath, _dirnames, _filenames) in os.walk(subdir):
        filenames.extend(_filenames)
        break

    filenames.sort()

    EnergyReal_WAC_Sum_Produced_per_day = []

    for filename in filenames:
        if 'dailysum' in filename:
            with open(os.path.join(subdir, filename)) as data_file:    
                data = json.load(data_file)

            if data['Body']['Data']:
                wac_sum_produced = float(data['Body']['Data']['inverter/1']['Data']['EnergyReal_WAC_Sum_Produced']['Values']['0'])/1000.0
                date = parse(data['Body']['Data']['inverter/1']['Start'])

                EnergyReal_WAC_Sum_Produced_per_day.append( (date.strftime("%y/%m/%d"), wac_sum_produced) )


    # no header text for the time column so that excel treats it as x axis values
    fieldnames = ['Date', 'EnergyReal_WAC_Sum_Produced_kWh']

    with open('examples/EnergyReal_WAC_Sum_Produced_per_day.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, dialect='excel-tab')
        writer.writerow(fieldnames)

        for date, wac_sum_produced in EnergyReal_WAC_Sum_Produced_per_day:
           writer.writerow([date, wac_sum_produced])


if __name__ == "__main__":
    main(sys.argv)
    #main(['', 'drosselweg'])


