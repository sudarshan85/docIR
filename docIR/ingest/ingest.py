#!/usr/bin/env python
"""
The ingest module processes a directory of documents, breaking them down into chunks of specified
length, limited by the context length of the conversational Large Language Model (LLM). Each chunk
is then embedded using a specified embedding model and the embeddings are stored in a vector
database
"""
import argparse
from typing import List
from pathlib import Path

__all__ = ['hello']

def hello(name: str) -> str:
  return f'Hello {name}! My name is ingest'

def parse_args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(description=__doc__,
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-n', '--name', type=str, help='Your name', default='Stranger')
  return parser.parse_args()

def entry_point() -> None:
  args = parse_args()
  print(hello(args.name))
