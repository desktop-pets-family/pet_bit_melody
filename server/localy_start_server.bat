@REM echo off
echo Creating python environment
py -m venv wenv
echo Activating python environment
wenv\Scripts\activate && ^
echo Installing requirements && ^
pip install -r requirements.txt && ^
echo Starting server && ^
py main.py --host 0.0.0.0 --port 5000  --debug && ^
echo Deactivating python environment && ^
deactivate
