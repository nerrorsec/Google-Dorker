#!usr/bin/env python

import requests
import webbrowser
import re

print ("                        ______                       _         _____                  _                   ")
print ("                       / _____)                     | |       (____ \                | |                  ")
print ("                      | /  ___   ___    ___    ____ | |  ____  _   \ \   ___    ____ | |  _   ____   ____ ")
print ("                      | | (___) / _ \  / _ \  / _  || | / _  )| |   | | / _ \  / ___)| | / ) / _  ) / ___)")
print ("                      | \____/|| |_| || |_| |( ( | || |( (/ / | |__/ / | |_| || |    | |< ( ( (/ / | |    ")
print ("                       \_____/  \___/  \___/  \_|| ||_| \____)|_____/   \___/ |_|    |_| \_) \____)|_|    ")
print ("                                             (_____|                       Coded By: _ __                 ")
print ("                                                                                    | '_ \                ")
print ("                                                                                    | | | |               ")
print ("                                                                                    |_| |_|_Error Dreamer ")
print ("\n\n")

url = input("Enter the URL: (Eg. example.com)\n >> ")
print("\n\n")

print ("Checking for Directory listing vulnerabilities")

url1 = "https://www.google.com/search?q=site:" + url + " intitle:index.of&hl=en"
dir = requests.get(url1)
found = re.search(r"\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\D.", (dir.content).decode("utf-8"))
captcha = re.search(r"\D\D\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\D\D\D\D\s\D\D\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\s\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D.", (dir.content).decode("utf-8"))

if found:
    print ("[-] Nothing found!")
elif captcha:
    print ("[-] Google is blocking the request. Try again after some time.")
else:
    print ("[+] Got some stuffs!")
    webbrowser.open(url1)
print("\n")

print ("Checking for Configuration files exposed")

url1 = "https://www.google.com/search?q=site:" + url + " ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini&hl=en"
conf = requests.get(url1)
found = re.search(r"\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\D.", (conf.content).decode("utf-8"))
captcha = re.search(r"\D\D\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\D\D\D\D\s\D\D\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\s\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D.", (conf.content).decode("utf-8"))

if found:
    print ("[-] Nothing found!")
elif captcha:
    print ("[-] Google is blocking the request. Try again after some time.")
else:
    print ("[+] Got some stuffs!")
    webbrowser.open(url1)
print("\n")

print ("Checking for Database files exposed")

url1 = "https://www.google.com/search?q=site:" + url + " ext:sql | ext:dbf | ext:mdb&hl=en"
db = requests.get(url1)
found = re.search(r"\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\D.", (db.content).decode("utf-8"))
captcha = re.search(r"\D\D\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\D\D\D\D\s\D\D\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\s\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D.", (db.content).decode("utf-8"))

if found:
    print ("[-] Nothing found!")
elif captcha:
    print ("[-] Google is blocking the request. Try again after some time.")
else:
    print ("[+] Got some stuffs!")
    webbrowser.open(url1)
print("\n")

print ("Checking for Log files exposed")

url1 = "https://www.google.com/search?q=site:" + url + " ext:log&hl=en"
log = requests.get(url1)
found = re.search(r"\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\D.", (log.content).decode("utf-8"))
captcha = re.search(r"\D\D\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\D\D\D\D\s\D\D\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\s\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D.", (log.content).decode("utf-8"))

if found:
    print ("[-] Nothing found!")
elif captcha:
    print ("[-] Google is blocking the request. Try again after some time.")
else:
    print ("[+] Got some stuffs!")
    webbrowser.open(url1)
print("\n")

print ("Checking for Backup and old files")

url1 = "https://www.google.com/search?q=site:" + url + " ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup&hl=en"
bak = requests.get(url1)
found = re.search(r"\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\D.", (bak.content).decode("utf-8"))
captcha = re.search(r"\D\D\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\D\D\D\D\s\D\D\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\s\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D.", (bak.content).decode("utf-8"))

if found:
    print ("[-] Nothing found!")
elif captcha:
    print ("[-] Google is blocking the request. Try again after some time.")
else:
    print ("[+] Got some stuffs!")
    webbrowser.open(url1)
print("\n")

print ("Checking for Login pages")

url1 = "https://www.google.com/search?q=site:" + url + " inurl:login&hl=en"
login = requests.get(url1)
found = re.search(r"\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\D.", (login.content).decode("utf-8"))
captcha = re.search(r"\D\D\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\D\D\D\D\s\D\D\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\s\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D.", (login.content).decode("utf-8"))

if found:
    print ("[-] Nothing found!")
elif captcha:
    print ("[-] Google is blocking the request. Try again after some time.")
else:
    print ("[+] Got some stuffs!")
    webbrowser.open(url1)
print("\n")

print ("Checking for SQL errors")

url1 = 'https://www.google.com/search?q=site:' + url + ' intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"&hl=en'
sql = requests.get(url1)
found = re.search(r"\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\D.", (sql.content).decode("utf-8"))
captcha = re.search(r"\D\D\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\D\D\D\D\s\D\D\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\s\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D.", (sql.content).decode("utf-8"))

if found:
    print ("[-] Nothing found!")
elif captcha:
    print ("[-] Google is blocking the request. Try again after some time.")
else:
    print ("[+] Got some stuffs!")
    webbrowser.open(url1)
print("\n")

print ("Checking for Publicly exposed documents ")

url1 = "https://www.google.com/search?q=site:" + url + " ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv&hl=en"
public = requests.get(url1)
found = re.search(r"\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\D.", str(public.content))
captcha = re.search(r"\D\D\D\D\D\D\D\s\D\D\D\s\D\D\D\D\D\s\D\D\D\D\D\D\D\s\D\D\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D\s\D\D\s\D\D\D\s\D\D\D\s\D\D\D\D\D\D\D\D.", str(public.content))

if found:
    print ("[-] Nothing found!")
elif captcha:
    print ("[-] Google is blocking the request. Try again after some time.")
else:
    print ("[+] Got some stuffs!")
    webbrowser.open(url1)

print("\n")
print ("                                   ##Please manually check for useful stuffs in the browser. Thanks :-)##")
print("\n")