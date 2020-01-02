import random
import utime

def populate_first_time():
  f = open("xpet.db", "w")
  db = {}
  
  ### PUT HOUR and MINUTE INTO THE SEED FROM WHAT USER INPUTS
  #random.seed()
  
  db["ttl"] = random.randint(1123200, 1728000)
  db["lifetime"] = 0
  db["stage"] = 0
  db["health"] = 8
  db["drink"] = 8
  db["food"] = 8
  db["sweets"] = 8
  db["fun"] = 8
  db["book"] = 8
  db["wash"] = 8
  db["sleep"] = 8
  
  for key in db:
    f.write(str(key) + ":" + str(db[key]) + "\n")
  
  f.close()
  
  read_db_value("ttl")
  
def read_db_value(parameter):
  f = open("xpet.db")
  
  for line in f:
    if line.startswith(parameter + ':'):
      result = line.split(":")[1].split("\n")[0]
    
  f.close()
  return result
  
def update_db_value(parameter, value):
  f = open("xpet.db")
  
  for line in f:
    if parameter in line:
      line.replace(parameter + ":" + str(value))
      
  f.close()
  
#def grow():
 
#def check_for_grow():
#  db = btree.open(f)
#  db
  
#populate_first_time()
#grow()


