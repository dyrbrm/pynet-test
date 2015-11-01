#!/usr/bin/env python

import yaml
import json
import pprint

with open("yaml_file.yml") as f:
   new_yaml_list = yaml.load(f)

with open("json_file.json") as f:
   new_json_list = json.load(f)

print "yaml file="
print new_yaml_list

print "json file="
print new_json_list
