import json
from pprint import pprint

filename = 'ne_110m_admin_0_countries_lakes'

# Move feature.bbox property to feature.properties.bbox
with open(filename + '.geojson') as data_file:
    data = json.load(data_file)

    for feature in data["features"]:
	    feature['properties']['bbox'] = feature['bbox']
	    del feature['bbox']

with open(filename + '_converted' + '.geojson', 'w') as output_file:
    json.dump(data, output_file)
