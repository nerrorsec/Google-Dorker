#!usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re
import optparse
import subprocess
import time

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Target URL")
    parser.add_option('-m', '--manual', help="Enables manual mode", action="store_true")
    (option, arguments) = parser.parse_args()
    if not option.url:
        parser.error("[-] Please specify an URL, use --help for more info")
    return option
options =  get_arguments()
url = options.url
print("\n\n")
subprocess.call(["chmod", "777", url + ".html"])
subprocess.call(["rm", url + ".html"])
subprocess.call(["clear"])
print("                        ______                       _         _____                  _                   ")
print("                       / _____)                     | |       (____ \                | |                  ")
print("                      | /  ___   ___    ___    ____ | |  ____  _   \ \   ___    ____ | |  _   ____   ____ ")
print("                      | | (___) / _ \  / _ \  / _  || | / _  )| |   | | / _ \  / ___)| | / ) / _  ) / ___)")
print("                      | \____/|| |_| || |_| |( ( | || |( (/ / | |__/ / | |_| || |    | |< ( ( (/ / | |    ")
print("                       \_____/  \___/  \___/  \_|| ||_| \____)|_____/   \___/ |_|    |_| \_) \____)|_|    ")
print("                                             (_____|                                      By: nerrorsec ")
print("\n\n")
f = open(str(url) + ".html", "at")
f.write(
    '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"> <title>Results from GoogleDorker by nerrorsec</title> </head> <body><br>')

if options.manual:
    def manual():
        global f
        print("[+]Registering data into the file.\n")
        time.sleep(2)
        f.write("<h2>Manual mode - Check the links manually.</h2>")
        f.write("<br>")
        f.write('<h2>Possible Directory listing</h2>')
        f.write('<a href="https://www.google.com/search?q=site:'+ url +'+intitle:index.of&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Configuration files</h2>')
        f.write('<a href="https://www.google.com/search?q=site:'+ url +'+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Database files</h2>')
        f.write('<a href="https://www.google.com/search?q=site:'+ url +'+ext:sql+|+ext:dbf+|+ext:mdb&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Log files</h2>')
        f.write('<a href="https://www.google.com/search?q=site:'+ url +'+ext:log&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Backup and Old files</h2>')
        f.write('<a href="https://www.google.com/search?q=site:'+ url +'+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Login pages</h2>')
        f.write('<a href="https://www.google.com/search?q=site:'+ url +'+inurl:login&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible SQL Errors</h2>')
        f.write('<a href="https://www.google.com/search?q=site:'+ url +'+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>Possible Publicly Exposed Documents</h2>')
        f.write('<a href="https://www.google.com/search?q=site:'+ url +'+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv&hl=en">Click Here</a>')
        f.write("<br>")
        f.write('<h2>phpinfo()</h2>')
        f.write('<a href="https://www.google.com/search?q=site:'+ url +'+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22&hl=en">Click Here</a>')
        f.write("<br>")
        f.close()
        print("File successfully created.\n")
    manual()

else:

    def process_google():
        global f
        print("Dorking via Google")
        print("\n")
        f.write("<h1>Results from Google</h1>")
        f.write("<br>")
        print ("[#]Checking for Directory listing vulnerabilities")
        requesturl = 'https://www.google.com/search?q=site:'+ url +'+intitle:index.of&hl=en'
        response = requests.get(requesturl)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Directory listing</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
        print ("[#]Checking for Configuration files exposed")
        requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini&hl=en'
        response = requests.get(requesturl)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Configuration files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
        print ("[#]Checking for Database files exposed")
        requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:sql+|+ext:dbf+|+ext:mdb&hl=en'
        response = requests.get(requesturl)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Database files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
        print ("[#]Checking for Log files exposed")
        requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:log&hl=en'
        response = requests.get(requesturl)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Log files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
        print ("[#]Checking for Backup and old files")
        requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup&hl=en'
        response = requests.get(requesturl)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Backup and Old files</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
        print ("[#]Checking for Login pages")
        requesturl = 'https://www.google.com/search?q=site:'+ url +'+inurl:login&hl=en'
        response = requests.get(requesturl)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Login pages</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
        print ("[#]Checking for SQL errors")

        requesturl = 'https://www.google.com/search?q=site:'+ url +'+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22&hl=en'
        response = requests.get(requesturl)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible SQL Errors</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
        print("[#]Checking for Publicly exposed documents ")
        requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv&hl=en'
        response = requests.get(requesturl)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>Possible Publicly Exposed Documents</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
        print("[#]Checking for phpinfo() ")
        requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22&hl=en'
        response = requests.get(requesturl)
        notfound = re.search('\s-\sdid not match any documents.', response.text)
        captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
        if notfound:
            print("[-]No results found\n")
        elif captcha:
            print("[-]Captcha triggered. Please try after some time.\n")
        else:
            print("[+]Registering data into the file.\n")
            f.write('<h2>phpinfo()</h2>')
            f.write('<a href="' + requesturl + '">Click Here</a>')
            f.write("<br>")
            f.close()

    process_google()
