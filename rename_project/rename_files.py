#!/usr/bin python3

"""Переименовать один из файлов.
Переименовать все файлы прибавив 1 в конец названия файла.
Переименовать все файлы прибавив 2 с использованием mv.
"""

import subprocess
from pathlib import Path

current_dir = Path(__file__).parent

ls = subprocess.run(
    [f'ls {current_dir.as_posix()} | egrep "*.txt"'],
    shell=True,
    capture_output=True,
    encoding='utf-8',
    check=True
    )

files = [current_dir / file for file in ls.stdout.strip().split('\n')]

# print(string)

# for file in files:
#     file.rename(
#         Path(file.parent, f'{file.stem.partition("_1")[0]}{file.suffix}')
#     )

for file in files:
    string = (
        f'mv {file} {file.parent}/{file.stem.replace("rename_project", "")}'
        f'{file.suffix}'
        )
    
    print(string)

    # res = subprocess.run(
    #     [f'{string}'],
    #     shell=True,
    #     capture_output=True,
    #     encoding='utf-8',
    #     check=True,
    # )
    # print(res.stderr)
    pass