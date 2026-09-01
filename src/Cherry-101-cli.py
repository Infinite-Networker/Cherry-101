#!/usr/bin/env python3
"""CLI for Cherry-101. Loads hyphenated src files as importable modules."""
import argparse
import importlib.util
import os
import sys

SRC = os.path.dirname(os.path.abspath(__file__))


def _load(modname, filename):
    path = os.path.join(SRC, filename)
    spec = importlib.util.spec_from_file_location(modname, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {filename} as {modname}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[modname] = mod
    spec.loader.exec_module(mod)
    return mod


_load("Cherry_101_parser", "Cherry-101-parser.py")
_load("Cherry_101_adapters", "Cherry-101-adapters.py")
_interp = _load("Cherry_101_interpreter", "Cherry-101-interpreter.py")
Runtime = _interp.Runtime


def _force_utf8_stdout():
    """Windows consoles default to cp1252 and crash on emoji in the example."""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main(argv=None):
    _force_utf8_stdout()
    p = argparse.ArgumentParser(description="Run a CherryScript (.cherry-101) program")
    p.add_argument("script", help="Path to the .cherry-101 script file")
    args = p.parse_args(argv)
    with open(args.script, encoding="utf-8") as f:
        src = f.read()
    rt = Runtime()
    rt.run(src)
    return 0


if __name__ == "__main__":
    sys.exit(main())
