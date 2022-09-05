
"""
Fetches and saves the results of some (important?) API endpoints
as reference examples. Can be used to see changes.
"""

import requests
import sys
import os
import json
import re

hostname = "fronius"
version = "1.23.2-1"

def get_example(endpoint):

	print("Fetching " + endpoint)

	url = "http://" + hostname + endpoint
	r = requests.get(url, timeout=60)
	r.raise_for_status()
	jsondata = r.json()

	m = re.match(r".*/(.*)\..*", endpoint)
	filename = m.group(1)

	directory = os.path.join("examples", "json", version)

	if not os.path.exists(directory):
		os.makedirs(directory)

	with open(os.path.join(directory, filename + ".json"), 'w') as f:
		json.dump(jsondata, f, indent=4, sort_keys=True)


def main(argv):

	get_example("/solar_api/v1/GetActiveDeviceInfo.cgi?DeviceClass=System")
	get_example("/solar_api/v1/GetInverterInfo.cgi")
	get_example("/solar_api/v1/GetInverterRealtimeData.cgi?Scope=System")
	get_example("/solar_api/v1/GetLoggerInfo.cgi")
	get_example("/solar_api/v1/GetLoggerLEDInfo.cgi")
	get_example("/solar_api/v1/GetMeterRealtimeData.cgi?Scope=System")
	get_example("/solar_api/v1/GetPowerFlowRealtimeData.fcgi")
	get_example("/solar_api/v1/GetStorageRealtimeData.cgi?Scope=System")

if __name__ == "__main__":
	main(sys.argv)

