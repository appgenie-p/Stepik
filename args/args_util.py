
import re
import sys


USAGE = "Usage: args_util [-s <separator>] [start [increment]] end"
ARGS = sys.argv[1:]
# ARGS = ["13"]

pattern = re.compile(
    r"""
        ^--(?P<HELP>help)|^-(?P<H>h)|
        \s?(?P<START>\d+)?
        \s(?P<INC>\d+)?
        \s(?P<END>\d+)$
    """, re.VERBOSE)

def main():
    """Increase start for increment val till the end.

    Implement empty args value, -h or --help shows USAGE info
    if end number provided print every digit from 1 to end incremented by 1
    """
    args_str = " ".join(ARGS)
    START, INC, END = 1, 1, 1

    if len(ARGS) == 0:
        print(USAGE)
        return

    args_passed = {
        k: v for k, v in pattern.match(args_str).groupdict().items() if v}
    
    help_full = args_passed.get("HELP")
    help_min = args_passed.get("H")
    start = int(args_passed.get("START", START))
    inc = int(args_passed.get("INC", INC))
    end = int(args_passed.get("END", END))
    
    if help_full or help_min:
        print(USAGE)
        return

    for i in range(start, end + 1, inc):
        print(i)



if __name__ == "__main__":
    main()