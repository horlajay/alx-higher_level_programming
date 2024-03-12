#!/usr/bin/python3
letters = range(97,123)
for c in letters:
    if chr(c) != 'e' and chr(c) !=  'q':
        print("{}".format(chr(c)), end=' ')
