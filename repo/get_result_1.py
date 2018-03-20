import subprocess

handle = open(r"..\rep_list.txt", "r")
for line in handle:
	command = "git clone "+line.strip()+".git"
	print(command )
	p = subprocess.Popen(command.split())	
handle.close()