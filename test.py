from SqliteHelper import *        

test = SqliteHelper("Content/database/database.db")

test.create_table_device()
test.create_table_token()
test.create_table_device_has_token()
test.create_table_position()

test.insert("INSERT INTO devices (name,ip,port,username,password,notify,status) VALUES ('Home 1','192.168.0.237','8090','admin','888888','Disable','Offline') ")
test.insert("INSERT INTO devices (name,ip,port,username,password,notify,status) VALUES ('Home 2','192.168.0.238','8090','admin','888888','Disable','Offline') ")
test.insert("INSERT INTO devices (name,ip,port,username,password,notify,status) VALUES ('Home 3','192.168.0.239','8090','admin','888888','Disable','Offline') ")

test.insert("INSERT INTO tokens (name,address) VALUES ('Group Alert 1','zNNUzZVu5ysu6GvcWqljXJ1SvOpmePWtqorx5QeoutK') ")
test.insert("INSERT INTO tokens (name,address) VALUES ('Group Alert 2','PM7Y596SX9SOR5XRTXas5F7vds1DonsFz8ABsCafDTW') ")
test.insert("INSERT INTO tokens (name,address) VALUES ('Group Alert 3','U2Te0etdWS1Dis5WwnK7uncYXtOGMF7nnfDstUYBFRJ') ")
test.insert("INSERT INTO tokens (name,address) VALUES ('1-1 Alert','uaF77tyhjzJnZy3o5GpvmeyY8n7zv4bpAB2TOU4WSjt') ")

test.insert("INSERT INTO device_has_token (device_name,token_name) VALUES ('Home 1','Group Alert 1') ")
test.insert("INSERT INTO device_has_token (device_name,token_name) VALUES ('Home 1','Group Alert 2') ")
test.insert("INSERT INTO device_has_token (device_name,token_name) VALUES ('Home 1','Group Alert 3') ")
test.insert("INSERT INTO device_has_token (device_name,token_name) VALUES ('Home 2','Group Alert 2') ")
test.insert("INSERT INTO device_has_token (device_name,token_name) VALUES ('Home 3','1-1 Alert') ")

test.insert("INSERT INTO position (device_name,position,address,ip,status) VALUES ('Home 1','POSITION_1','บ้านเลขที่  98/31','192.168.0.202','Offline') ")
test.insert("INSERT INTO position (device_name,position,address,ip,status) VALUES ('Home 1','POSITION_2','บ้านเลขที่  98/33','192.168.0.203','Offline') ")
test.insert("INSERT INTO position (device_name,position,address,ip,status) VALUES ('Home 2','POSITION_3','บ้านเลขที่  98/57','192.168.0.204','Offline') ")
test.insert("INSERT INTO position (device_name,position,address,ip,status) VALUES ('Home 2','POSITION_4','บ้านเลขที่  98/55','192.168.0.205','Offline') ")
test.insert("INSERT INTO position (device_name,position,address,ip,status) VALUES ('Home 3','POSITION_5','บ้านเลขที่  98/00','192.168.0.206','Offline') ")
test.insert("INSERT INTO position (device_name,position,address,ip,status) VALUES ('Home 3','POSITION_6','บ้านเลขที่  98/00','192.168.0.207','Offline') ")



#test.edit("UPDATE tokens SET name='jack' WHERE name = 'john'")
#print(test.select("SELECT * FROM tokens"))

##test.edit("DELETE from devices where id=22;")
#test.edit("DROP TABLE devices;")
#test.delete("DROP TABLE position;")

#test.edit("UPDATE tokens SET name='jack' WHERE name = 'john'")
#print(test.select("SELECT * FROM tokens"))