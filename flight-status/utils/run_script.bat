@echo off
REM Set the path to your virtual environment and the Python file
set VENV_PATH=C:\Users\ACER\Desktop\indigo_flight_status\flight-status\.venv
set PYTHON_FILE=C:\Users\ACER\Desktop\indigo_flight_status\flight-status\utils\track_flight.py

REM Activate the virtual environment
call %VENV_PATH%\Scripts\activate.bat

REM Run the Python file
python %PYTHON_FILE%

REM Deactivate the virtual environment (optional)
deactivate
