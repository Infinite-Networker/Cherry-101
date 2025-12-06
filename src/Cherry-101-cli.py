#!/usr/bin/env python3
import argparse
from cherryscript.runtime.interpreter import Runtime
p=argparse.ArgumentParser(); p.add_argument('script'); args=p.parse_args()
with open(args.script) as f: src=f.read()
rt=Runtime(); rt.run(src)
