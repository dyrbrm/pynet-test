#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

with open("cisco_ipsec.txt") as f:
   cfg = CiscoConfParse(f)

cfg_crypto = cfg.find_objects('crypto map')
print "--- all entries with crypto map ---"
for element in cfg_crypto:
   print "\n", element, "\n"
   print element.children

cfg_crypto = cfg.find_objects_w_child(parentspec='crypto map', childspec='pfs group2')
print "--- all entries with crypto map and pfs group2 ---"
for element in cfg_crypto:
   print "\n", element, "\n"
   print element.children

cfg_crypto = cfg.find_objects_wo_child(parentspec='crypto map', childspec='AES')
print "--- all entries with crypto map and without AES ---"
for element in cfg_crypto:
   print "\n", element, "\n"
   print element.children
