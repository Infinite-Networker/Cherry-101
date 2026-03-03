#!/usr/bin/env python3
import sys
import argparse
from Cherry_101_interpreter import Runtime
p = argparse.ArgumentParser(description='Run a CherryScript (.cherry-101) program')
p.add_argument('script', help='Path to the .cherry-101 script file')
args = p.parse_args()
with open(args.script) as f:
    src = f.read()
rt = Runtime()
rt.run(src)
