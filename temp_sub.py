import subprocess
import shlex

completed_process = subprocess.run(
        shlex.split('python3 timer.py'), check=True)
completed_process.returncode
