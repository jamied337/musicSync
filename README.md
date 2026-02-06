# musicSync
simple script to sync music libraries

This script works by copying a library of .flac files to another location and converting them to .mp3 files while retaining metadata such as title, album, artist, track number, and album art.

Dependancies:
  pathlib
  mutagen
  pydub

  Installation on most systems: pip install pathlib mutagen pydub 
  Installation on arch-based systems: sudo pacman -S python-pathlib python-mutagen python-pydub

Usage:
  python3 musicSync.py
    
