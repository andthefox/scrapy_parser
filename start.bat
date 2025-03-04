@echo off

echo Creating virtual environment...

python -m venv venv

echo Downloading packages...

call venv/Scripts/activate && python -m pip install --upgrade pip && pip install -r requirements.txt 

echo Running parser...

call venv/Scripts/activate && scrapy crawl insta

echo Done! =)

%SystemRoot%\explorer.exe "results"

pause
