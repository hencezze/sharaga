import re
import sys

# Take any string data
PATTERN = '^[A-Z]'
word=input()
# match the pattern with input value
found = re.match(PATTERN,word )

# Print message based on the return value
if found:
    print("DA")
else:
    print("NET")
