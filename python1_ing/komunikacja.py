#!/usr/bin/python
import sys
import os

#stdout, stderr i stdin
sys.stdout.write("hello world!\n")
sys.stdout.flush()
if len(sys.argv)<=1:
    inp = sys.stdin.read()
    print(inp,file=sys.stderr)

#sys.stdout.write(inp)
#modul argparse
print(sys.argv)

#zmienne srodowiskowe
print(os.environ)

#exit code/errorlevel
sys.exit(3)