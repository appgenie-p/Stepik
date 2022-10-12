import sys

try:
    arg = sys.argv[1]
except IndexError:
    raise  SystemExit(f"Usage: {sys.argv[0]} <string_to_reverse>")

print(arg[::-1])