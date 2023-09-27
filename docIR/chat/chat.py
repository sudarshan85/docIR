#!/usr/bin/env python
"""
The chat module is a Q&A chat model that uses the input question as a context, performs semantic
search, and uses large language model (LLM) to synthesize an answer. The chatbot will allow history
and followup questions.
"""
import argparse
from pathlib import Path

__all__ = ['hello']

def hello(name: str) -> str:
  return f'Hello {name}! My name is chat'

def parse_args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(description=__doc__,
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-n', '--name', type=str, help='Your name', default='Stranger')
  return parser.parse_args()

def entry_point() -> None:
  args = parse_args()
  print(hello(args.name))


