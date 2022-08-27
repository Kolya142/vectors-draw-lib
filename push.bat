@echo off
python3 -m build
set /p build = test_build?
if %build%==y (python3 -m twine upload --repository testpypi dist/*)
if %build%==n (python3 -m twine upload dist/*)