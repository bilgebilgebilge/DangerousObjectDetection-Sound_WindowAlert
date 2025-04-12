@echo off

:: Check if Python is installed
python --version >nul 2>nul || (
    echo Python is not installed! Please install Python from: https://www.python.org/downloads/
    pause
    exit /b
)

:: Check if the virtual environment exists, if not create it
if not exist "venv" (
    echo Virtual environment not found. Creating one now...
    python -m venv venv
)

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies from requirements.txt if not already installed
pip install -r requirements.txt

:: Open VS Code with the project folder
code .

:: Run the main Python script
python main.py

pause
