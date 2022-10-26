
from datetime import datetime
import fnmatch
import os
from pathlib import Path
import re


def convert_time(timestamp):
    time = datetime.utcfromtimestamp(timestamp)
    return time.strftime('%m/%d/%Y, %H:%M:%S')


def get_files(path = ''):
    for entry in Path(path).iterdir():
        info = entry.stat()
        print(f'{entry.name}\t Last Modified: {convert_time(info.st_mtime)}')


def file_search(path = ''):
    for entry in Path(path).glob('*'):
            print(entry)
        

if __name__ == '__main__':
    file_search()