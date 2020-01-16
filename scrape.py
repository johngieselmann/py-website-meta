#!/usr/local/bin/python3

import sys
import re

# make sure we have the required arguments
if not sys.argv[1]:
    print("Website is required")
    sys.exit()
else:
    arg1 = sys.argv[1]

# check if we are asking for help or ready to party
if arg1 == "--help" or arg1 == "-h":
    print("scrape.py <website>\n\n")
    sys.exit()
else:
    site = sys.argv[1]

# validate the website
if not re.match("^((https?):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$", site):
    print("Not a valid website")
    sys.exit()
else:
    print("Valid URL")


print("done")
