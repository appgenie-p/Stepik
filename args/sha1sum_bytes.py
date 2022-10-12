import os
import sys
import hashlib

data = os.fsencode(sys.argv[1])
m = hashlib.sha1()
m.update(data)
print(m.hexdigest())
