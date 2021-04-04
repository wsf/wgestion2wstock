copy C:\wsf\wgestionvolken\wgestion_wstock.txt 


REM actualizo la base de datos 

REM bajo la ultima copia de la base de datos
git pull

REM restauro la copia

mysql -uroot -pdalas.2009 wstockprodu < wstockprodu.sql 

REM Subo los cambios de stock para que horacio lo pueda bajar.

git add wgestion_wstock.txt
git -m "subiendo actualización"
git push



