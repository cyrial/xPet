import random
import utime

db = {}

def populate_first_time():
  global db
  
  f = open("xpet.db", "w")  
  
  ### PUT HOUR and MINUTE INTO THE SEED FROM WHAT USER INPUTS
  #random.seed()
  
  db["ttl"] = random.randint(1123200, 1728000)
  db["lifetime"] = 0
  db["stage"] = 0
  db["health"] = 10
  db["drink"] = 9
  db["food"] = 8
  db["sweets"] = 7
  db["fun"] = 4
  db["book"] = 3
  db["wash"] = 2
  db["sleep"] = 0
  
  db["time_poo"] = 0

  for key in db:
    f.write(str(key) + ":" + str(db[key]) + "\n")
  
  f.close()
  
  read_db_value("ttl")
  
def read_db_value(parameter):
  global db
  
  f = open("xpet.db")
  
  for line in f:
    if line.startswith(parameter + ':'):
      result = line.split(":")[1].split("\n")[0]
    
  f.close()
  return result
  
def update_db_value(parameter, value):
    global db
    
    f = open("xpet.db", "w")
    
    for key in db:
        if key == parameter:
            f.write(str(key) + ":" + str(value) + "\n")
            db.update({key:value})
        else:
            f.write(str(key) + ":" + str(db[key]) + "\n")
            db.update({key:db[key]})
    f.close()
