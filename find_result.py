import re

handle = open(r"res.txt", "r")
data = handle.read()
#substr_1 = '[INFO] Reactor Build Order:'
#strart_pos = data.find(substr_1)
#print strart_pos 
#matched_lines = [line for line in data.split('\n') if substr_1 in line]
#print matched_lines
#print data
regexpr = "^\[INFO\] Reactor Build Order:$([^.$]*)^\[INFO\] ---------------------"
regexpr = "Reactor Build Order"
p = re.compile(regexpr, re.MULTILINE)
print p.match(data)