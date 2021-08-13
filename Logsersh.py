#Thi is a Python file to run query  on access logs

logfile = r"/home/pi/log/access_log"

important = []
keep_phrases = ["162.211.82.115",	#add IP for the Attaker as much as you could
              "31.210.20.127",
              "54.221.13.46"]

with open(logfile) as l:
    l = l.readlines()

for line in l:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break

print(important)		#to print only the important

