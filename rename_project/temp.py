
import os
from pathlib import Path


dir = Path()

for entry in dir.iterdir():
    print(entry.name)