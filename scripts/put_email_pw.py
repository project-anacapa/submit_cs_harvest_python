#!/usr/bin/env python

import requests
import pprint
import sys


def main(password):
  payload = {'email': 'chilloien@gmail.com', 'password': password}
  r = requests.put('https://submit.cs.ucsb.edu/session', data=payload)

  print r.text


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " password"
        sys.exit()
        
    main(sys.argv[1])
