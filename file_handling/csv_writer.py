import csv

with open("ipl.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["CSK","MI","GT","RCB"])
    w.writerow(["MSD","RO","HP","VK"])
f=open("ipl.csv","r")
r=csv.reader(f)
print(list(r))