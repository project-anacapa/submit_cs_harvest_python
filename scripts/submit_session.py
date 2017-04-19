#!/usr/bin/env python

import requests
import pprint
import sys
import json




def main(password):

  s = requests.Session()

  payload = {'email': 'chilloien@gmail.com', 'password': password}

  r = s.put('https://submit.cs.ucsb.edu/session', data=json.dumps(payload))

  print r.text

  r2 = s.get("https://submit.cs.ucsb.edu/user/chilloien%40gmail.com")

  print r2.text

  projects = [705, 706, 707, 708, 709];

  for p in projects:

    url = "https://submit.cs.ucsb.edu/p/" + str(p) + "/info"
    print "Getting project number " + str(p) + " with url " + url

    r3 = s.get(url)
    print r3.text

    asDict = json.loads(r3.text)
    pprint.pprint(asDict)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " password"
        sys.exit()
        
    main(sys.argv[1])
