call .venv\Scripts\activate.bat

python mibei.py https://www.mibei77.com

python renumber.py

::python fetch.py

git commit -a -m "update" --quiet

if %errorlevel% equ 0 (
	git push
)

exit