first, second = input().split()
try:
    first, second = [int(val) for val in (first, second)]
except Exception:
    try:
        first, second = [float(val) for val in (first, second)]
    except Exception:
        pass
finally:
    print(first + second)
