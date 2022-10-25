
from pathlib import Path


files_in_basepath = (entry for entry in Path().iterdir() if entry.is_file())

for entry in files_in_basepath:
    print(entry.name)
    
pass