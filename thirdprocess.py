import os
import subprocess
import urllib

command = "java -jar"
jar = "selenium-server-standalone-3.141.59.jar"
action = command + jar
flag = True
jar_files = subprocess.Popen(['jps', '-l'], stdout=subprocess.PIPE).stdout.readlines()
run_jar_cmd = urllib.quote("'" + action + "'")

for jars in jar_files:
    output = jars.decode()
    if output.__contains__(jar):
        flag = False
if flag:
    os.system('cmd /k' + run_jar_cmd)
else:
    print("Already The Selenium Jar Is Running")
