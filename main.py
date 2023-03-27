# Import re module
import re
import sys

# Take any string data
PATTERN = '^[A-Z]'

# match the pattern with input value
found = re.match(PATTERN, sys.argv[0])

# Print message based on the return value
if found:
    print("DA")
else:
    print("NET")
