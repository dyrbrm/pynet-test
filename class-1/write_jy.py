#!/usr/bin/env python

import yaml
import json

my_list = []
for i in range (5):
   my_list.append(i)

my_list.append({})
my_list[-1]['platform'] = 'arista'
my_list[-1]['ip_addr'] = '10.0.0.1'
my_list[-1]['attribs'] = range(10)

with open("yaml_file.yml", "w") as f:
   f.write(yaml.dump(my_list, default_flow_style=False))

with open("json_file.json", "w") as f:
   json.dump(my_list, f)
