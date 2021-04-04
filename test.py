#imports
import requests
import pymysql.cursors
import logging as log
import datetime

#declaraciones
log.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', \
                    level = log.DEBUG, filename = "log.log")



j = {}

j = eval(open("config.txt","r").read())

print(j)

db = pymysql.connect(host=j["host"], user=j["user"], passwd=j["passwd"], db=j["db"])
cur = db.cursor()


#funciones 


def prove_sql():
    global cur
    sql = "select * from stock limit 10"
    cur.execute(sql)
    r = cur.fetchall()
    print(r)

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
                        
                except Exception as e:
                        log.error(e)


        open("last_reg.txt","w").write(str(i))

        log.info("**** Datos procesados del archivo <wgestion_wstock.txt>. Comienza en la linea: %s, termina en la linea: %s " % (str(last_reg), str(i)) )
        
       


if __name__ == "__main__":
        init()
        prove_sql()
        load_file()
        