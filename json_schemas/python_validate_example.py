#!/usr/bin/env python

from jsonschema import validate
import json


def loadJSON(filename):
    contents = open(filename, 'r').read()
    return json.loads(contents)
    
schema = loadJSON('submit_cs_project.json')
p708 = loadJSON('examples/p708.json')
validate(p708,schema)

