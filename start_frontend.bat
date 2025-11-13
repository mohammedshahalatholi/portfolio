@echo off
echo Starting Frontend Server...
echo.
cd frontend
echo Starting server on http://localhost:3001
echo.
python -m http.server 3001
pause

