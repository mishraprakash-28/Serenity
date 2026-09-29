@echo off
title Serenify Setup and Launch
echo Installing required libraries from requirements.txt...
pip install -r requirements.txt
echo Setup complete. Launching application...
streamlit run app.py
pause