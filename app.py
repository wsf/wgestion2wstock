#imports
import requests
import pymysql.cursors
import logging as log
import datetime

from os import system

try:
        system("cls")
except:
        pass

#declaraciones
log.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', \
                    level = log.DEBUG, filename = "log.log")



j = {}

j = eval(open("config.txt","r").read())

#print(j)

db = pymysql.connect(host=j["host"], user=j["user"], passwd=j["passwd"], db=j["db"])
cur = db.cursor()


#funciones 

def make_update(sql):
    global cur
    cur.execute(sql)
    db.commit()
    
global last_reg
last_reg = 0

def init():
        # ultimo registro registrado
        global last_reg
        global arch_last_reg
        #arch_last_reg = open("last_reg.txt","r")
        
        last_reg = eval(open("last_reg.txt","r").read())
        

def load_file():
        url = "https://raw.githubusercontent.com/wsf/wgestion2wstock/main/wgestion_wstock.txt"

        data_arch = requests.get(url).text

        i = 0 
        
        for l in data_arch.split("\n"):
                i +=1

                if i<=last_reg:
                        continue

                try: 
                        ll = eval(l)
                        sql = ll[3]

                        log.info(sql)

                        if j["debug"].upper() == "SI":
                                make_update(sql)

                except Exception as e:
                        
                        # if an error occurs i register that 
                        log.error(e)

        open("last_reg.txt","w").write(str(i))

        log.info("**** Datos procesados del archivo <wgestion_wstock.txt>. Comienza en la linea: %s, termina en la linea: %s " % (str(last_reg), str(i)) )

        print("\n\n\n-----------------------")
        print("Se actualizó el stock de %s artículos " % str((i - last_reg)) )
        print("-----------------------")
        input("Presione una tecla para continuar")
        
       


if __name__ == "__main__":
        init()
        load_file()