import os
from chromadb.config import Settings 
from  chromadb import chromadb as Chroma
CHROMA_SETTINGS=Settings(
    chroma_db_impl='duckdb+parquet',
    persist_directory='db',
    anonymized_telemetry = False
)

