import os
import string
path = '.\\repo'
str = ''

for item in os.listdir(path):
    if not os.path.isfile(os.path.join(path, item)):
        #print "Folder: ",item
		str =  str + "<module>../"+ item +"</module>"+"\n"
		
print  str

handle = open("./pom_pattern.xml", "r")
data = handle.read()
str  = string.replace(data,"*REPLACEME*", str)
print str
handle.close()

handle = open("./superproject/pom.xml", "w")
handle.write(str)
handle.close()

