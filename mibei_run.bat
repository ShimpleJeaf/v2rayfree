call venv\Scripts\activate.bat

python mibei.py https://www.mibei77.com

git commit -a -m "update" --quiet

if %errorlevel% equ 0 (
	git push
)

exit