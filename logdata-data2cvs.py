import json
import csv
import collections

from pprint import pprint

with open('examples/logdata-data20160913235000.json') as data_file:    
    data = json.load(data_file)

#pprint(data)
#print(data['Body']['inverter/1']['Data']['Current_DC_String_1']['Values'])

values = data['Body']['inverter/1']['Data']['Current_DC_String_1']['Values']
orderedValues = collections.OrderedDict(sorted(values.items()))


with open('examples/logdata-data20160913235000.json.csv', 'wb') as csvfile:
    #data_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #data_writer.writerow(data['Body']['inverter/1']['Data']['Current_DC_String_1']['Values'])

    fieldnames = orderedValues.keys()

    data_writer = csv.DictWriter(csvfile, dialect='excel', fieldnames=fieldnames)
    data_writer.writeheader()
    data_writer.writerow(orderedValues)