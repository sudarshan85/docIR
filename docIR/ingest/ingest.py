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
from collections import defaultdict

from llama-index import SimpleDirectoryReader

__all__ = ['hello', 'IngestionEngine']

class IngestionEngine(object):
  def __init__(self, doc_dir: Path, db_dir: Path, db_type='chromadb'):
    self.doc_dir = doc_dir
    self.db_dir = db_dir
    self.db_type = db_type
    
  def read_documents(self):
    reader = SimpleDirectoryReader(input_dir=self.doc_dir)
    return reader.load_data()
    
  def count_docs(docs):
    count = defaultdict(int)
    doc_list = set()
    pages = defaultdict(int)
    
    for doc in docs:
      name = doc.metadata['file_name']
      pages[name] += 1
      ext = name.split('.')[-1]
      if name not in doc_list:
        doc_list.add(name)
        count[ext] += 1
        
    self.n_pages = sum([v for _,v in pages.items()])
    self.doc_list = doc_list
    self.n_docs_by_type = count
    
  def run(self):
    docs = self.read_docs()
    self.count_docs(docs)

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
