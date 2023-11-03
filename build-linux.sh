#!/bin/bash
echo "locating source"
cd source
echo "compiling..."
python3 -m PyInstaller --onefile sketch.py
echo "done"