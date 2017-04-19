#!/usr/bin/env python

import requests
import pprint

r = requests.get('https://submit.cs.ucsb.edu')

print r.text
