from pathlib import Path
from tempfile import TemporaryDirectory, TemporaryFile


# with TemporaryFile() as temp_file:
#     temp_file.write(b'test for test')
#     temp_file.seek(0)
#     data = temp_file.read().decode('utf-8')

# print(data)

with TemporaryDirectory() as tmpdir:
    print("Created temporary directory ", tmpdir)
    Path(tmpdir).is_dir()

Path(tmpdir).is_dir()
