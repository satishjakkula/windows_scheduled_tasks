import os
import subprocess

required = "selenium-server-standalone-3.141.59.jar"
flag = True
jar_files = subprocess.Popen(['jps', '-l'], stdout=subprocess.PIPE).stdout.readlines()

for jars in jar_files:
    output = jars.decode()
    print(output)
    if output.__contains__(required) or output.__contains__("process information unavailable"):
        flag = False
if flag:
    os.system('cmd /k "java -jar selenium-server-standalone-3.141.59.jar"')
else:
    print("Already The Selenium Jar Is Running")



