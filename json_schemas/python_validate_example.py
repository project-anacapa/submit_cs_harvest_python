#!/usr/bin/env python

from jsonschema import validate
import json

schema = json.loads('''
    {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title":"submit-cs-project",
    "type":"object",
    "properties" : {
	"id": {"type":"number"} 
    },
    "required" : ["id"]   
}
''')
    
p708 = json.loads('''
{
  "id": 708,
  "testables": {
    "Run lab02Tests.py and lab05Tests.py tests": {
      "test_cases": {
        "Run lab05Tests.py (student version)": {
          "stdin": null,
          "args": "bash .\/removeTestTiming.sh lab05Tests.py",
          "output_filename": null,
          "source": "stdout",
          "expected": "a717055ae7ab66e18e9295adbd6eacf1ccef305d",
          "output_type": "diff",
          "id": 9090
        },
        "Run lab02Tests.py (instructor version)": {
          "stdin": null,
          "args": "bash .\/removeTestTiming.sh lab02Tests.py",
          "output_filename": null,
          "source": "stdout",
          "expected": "119dadaa7e84ee684d54001da89b521a728e0bb6",
          "output_type": "diff",
          "id": 9088
        },
        "Run lab05Tests2.py (instructor version)": {
          "stdin": null,
          "args": "bash .\/removeTestTiming.sh lab05Tests2.py",
          "output_filename": null,
          "source": "stdout",
          "expected": "a717055ae7ab66e18e9295adbd6eacf1ccef305d",
          "output_type": "diff",
          "id": 9089
        }
      },
      "id": 2012
    },
    "Check syntax of student submitted Python files": {
      "test_cases": {
        "lab05Funcs.py file should have no syntax errors": {
          "stdin": null,
          "args": "python lab05Funcs.py",
          "output_filename": null,
          "source": "stderr",
          "expected": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
          "output_type": "diff",
          "id": 9087
        },
        "lab05Tests.py file should have no syntax errors": {
          "stdin": null,
          "args": "python -m py_compile lab05Tests.py",
          "output_filename": null,
          "source": "stderr",
          "expected": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
          "output_type": "diff",
          "id": 9086
        },
        "lab02Funcs.py file should have no syntax errors": {
          "stdin": null,
          "args": "python lab02Funcs.py",
          "output_filename": null,
          "source": "stderr",
          "expected": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
          "output_type": "diff",
          "id": 9085
        }
      },
      "id": 2011
    }
  },
  "name": "ccs_cs20_s16_lab05"
}
''')
                  
validate(p708,schema)

