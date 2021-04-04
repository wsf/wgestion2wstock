@echo off
cls
echo Date format = %date%
echo dd = %date:~0,2%
echo mm = %date:~3,2%
echo yyyy = %date:~6,4%
echo.
echo Time format = %time%
echo hh = %time:~0,2%
echo mm = %time:~3,2%
echo ss = %time:~6,2%
echo.
echo Timestamp = %date:~6,4%-%date:~3,2%-%date:~0,2%-%time:~0,2%-%time:~3,2%-%time:~6,2%

mysqldump -u root -pdalas.2009  -h 192.168.1.50  --databases --routines --verbose wstockprodu > bk\bk_wstockprodu-%date:~0,2%.sql
copy bk\bk_wstockprodu-%date:~0,2%.sql bk_wstockprodu.sql


#git pull

echo Comienza el traspaso de información
python app.py

REM actualizar bk_wstockprodu.sqlen github
git add bk_wstockprodu.sql
git commit -m "actualizando bk_wstockprodu.sql
git push
