from pathlib import Path
import sys

# arg = sys.argv[1]

def rem_file(file):
    try:
        Path(file).unlink()
    except FileNotFoundError:
        print('Введите корректое имя файла')
    except IsADirectoryError:
        print('Введите называние файла, а не дирректорию')



if __name__ == '__main__':
    rem_file(sys.argv[1])