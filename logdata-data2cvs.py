import json
import csv

from pprint import pprint

with open('examples/logdata-data20160913235000.json') as data_file:    
    data = json.load(data_file)

pprint(data)

with open('examples/logdata-data20160913235000.json.csv', 'wb') as csvfile:
    data_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['Body']['inverter/1']['Data']['Current_DC_String_1']['Values'])
