import subprocess


cmd = """mkdir some_directory &&
cd some_directory/ &&
mkdir sub_dir &&
touch sub_dir/file1.py sub_dir/file2.py &&
touch data_{01..03}.txt data_{01..03}_backup.txt admin.py tests.py
""".strip()

res = subprocess.run(
    [cmd], shell=True, executable="/bin/bash", capture_output=True, check=True
)
