#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        p = fct(*args)
    except (ValueError, ZeroDivisionError, IndexError, TypeError) as err:
        print("Exception:", err, file=sys.stderr)
        return None
    return p
