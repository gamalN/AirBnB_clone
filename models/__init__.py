#!/usr/bin/python3
"""
create global instance of FileStorage for all data models
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
