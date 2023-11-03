@echo off
echo locating source
cd source
echo compiling...
python -m PyInstaller --onefile sketch.py
echo moving to release folder
move %~dp0\source\dist\sketch.exe %~dp0\release\Windows
echo creating contents folder
mkdir %~dp0\release\Windows\Sketch-Library
echo copying contents
copy %~dp0\source\Sketch-Library %~dp0\release\Windows\Sketch-Library
echo done
pause