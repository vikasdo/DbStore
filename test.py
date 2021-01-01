from pack.abc import dbstore

import concurrent.futures
import time,threading

start = time.perf_counter()

threads = []
obj=dbstore()

# This loop is to add Keys in DB STORE
for i in range(4):
    
    secs = [('name','vikas',113),('street','canal lane',3),('city','hyderabad',2),('phone2',9392322121,322),('states','Telangana',1)]
    # obj.add(secs[i][0],secs[i][1],secs[i][2])
    t = threading.Thread(target=obj.add , args=[secs[i][0],secs[i][1],secs[i][2]])
    t.start()
    
    threads.append(t)

for thread in threads:
    thread.join()


# This loop is to READ Keys in DB STORE

for i in range(4):
    
    secs = [('name','vikas',0),('street','canal lane',3),('city','hyderabad',2),('phone2',9392322121,322),('states','Telangana',1)]
    # obj.add(secs[i][0],secs[i][1],secs[i][2])
    t = threading.Thread(target=obj.read , args=[secs[i][0],secs[i][1],secs[i][2]])
    t.start()
    
    threads.append(t)

for thread in threads:
    thread.join()


# This loop is to DELETE Keys in DB STORE

for i in range(1):
    
    secs = [('state','Telangana',1)]

    t = threading.Thread(target=obj.delete , args=[secs[i][0],secs[i][1],secs[i][2]])

    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
finish = time.perf_counter()

#measure The Performance of it...
print(f'Finished in {round(finish-start, 2)} second(s)')