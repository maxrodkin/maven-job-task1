import subprocess
import os

command = "mvn -v"
p = subprocess.Popen(r"mvn validate".split(),cwd=r"./superproject",shell=True, stdout = subprocess.PIPE)
#p = subprocess.Popen(r"cd ./superproject; mvn validate")
#p = subprocess.Popen(command.split())
#print(os.environ['JAVA_HOME'])
#p = subprocess.Popen(command.split(), stdin =     subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
res = p.stdout.read(-1)
print res.find('[INFO] Reactor Build Order:')
#print p.stdin.read(-1)
#print p.stderr.read(-1)

