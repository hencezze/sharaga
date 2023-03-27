# Import re module
import re
import sys

# Take any string data
PATTERN = '^[A-Z]'

# match the pattern with input value
found = re.match(PATTERN, sys.argv[0])

# Print message based on the return value
if found:
    print("The input value is started with the capital letter")
else:
    print("You have to type string start with the capital letter")
