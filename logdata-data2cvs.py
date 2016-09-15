import json
import csv
import collections

from pprint import pprint

with open('examples/logdata-data20160913235000.json') as data_file:    
    data = json.load(data_file)

#pprint(data)
#print(data['Body']['inverter/1']['Data']['Current_DC_String_1']['Values'])

c_dc_1_values = data['Body']['inverter/1']['Data']['Current_DC_String_1']['Values']

# Dictionaraies, returned by the json reader, have no order.
# So, convert it to a list of key/value tupels (.items()) and
# sort it with sorted(), using a lambda function to convert the key/first tupel item to an integer
# so that the sorting is based on numbers not text
c_dc_1_values_ordered = sorted(c_dc_1_values.items(), key=lambda x: int(x[0]) )

# no header text for the time column so that excel treats it as x axis values
fieldnames = ['', 'Current_DC_String_1']

with open('examples/logdata-data20160913235000.json.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, dialect='excel-tab')
    writer.writerow(fieldnames)

    for key, value in c_dc_1_values_ordered:
       writer.writerow([key, value])
