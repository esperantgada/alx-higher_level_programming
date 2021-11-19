#!/usr/bin/python3
if __name__ == "__main__":
    import sys
r, i = 0, 0
for arg in sys.argv:
    if (i > 0):
        r = r + int(arg)
    i = i + 1
print(r)
