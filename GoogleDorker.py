#!usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re
import optparse
import subprocess
import time

#################################################### Intro #################################################################


print("                        ______                       _         _____                  _                   ")
print("                       / _____)                     | |       (____ \                | |                  ")
print("                      | /  ___   ___    ___    ____ | |  ____  _   \ \   ___    ____ | |  _   ____   ____ ")
print("                      | | (___) / _ \  / _ \  / _  || | / _  )| |   | | / _ \  / ___)| | / ) / _  ) / ___)")
print("                      | \____/|| |_| || |_| |( ( | || |( (/ / | |__/ / | |_| || |    | |< ( ( (/ / | |    ")
print("                       \_____/  \___/  \___/  \_|| ||_| \____)|_____/   \___/ |_|    |_| \_) \____)|_|    ")
print("                                             (_____|                             By: nError#NSL ")
print("\n\n")


################################# Getting arguments #################################################################

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Target URL")
    (option, arguments) = parser.parse_args()
    if not option.url:
        parser.error("[-] Please specify an URL, use --help for moe info")
    return option

# url = input("Enter the URL: (Eg. example.com)\n >> ")
url = get_arguments().url
# print(url)
print("\n\n")
subprocess.call(["chmod", "777", url + ".html"])
subprocess.call(["rm", url + ".html"])

f = open(str(url) + ".html", "at")
f.write('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"> <title>Results from GoogleDorker by nError#NSL</title> </head> <body><br>')

def process_bing():

    global f
    
    print("Dorking via Bing")
    print("\n")

    f.write('<h1>Results from Bing</h1>')
    f.write('<br>')

    ############################################### Directory listing #######################################################

    print ("[#]Checking for Directory listing vulnerabilities")

    requesturl = 'https://www.bing.com/search?q=site:"' + url + '" intitle:index.of&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('There are no results for\s', response.text)
    # captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
        f.write('<h2>Results from Bing</h2>')
        f.write('<br>')
    # elif captcha:
    #     print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Results from GoogleDorker by nError#NSL</title> </head> <body><br>')
        f.write('<h2>Possible Directory listing</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ########################################################### Config files ################################################

    print ("[#]Checking for Configuration files exposed")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('There are no results for\s', response.text)
    # captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    # elif captcha:
    #     print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Configuration files</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ################################################## DB files #######################################################!

    print ("[#]Checking for Database files exposed")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:sql | ext:dbf | ext:mdb&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('There are no results for\s', response.text)
    # captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    # elif captcha:
    #     print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Database files</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ###################################################### Log files ####################################################

    print ("[#]Checking for Log files exposed")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:log&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('There are no results for\s', response.text)
    # captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    # elif captcha:
    #     print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Log files</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ########################################################## Backup and old files ###########################################

    print ("[#]Checking for Backup and old files")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('There are no results for\s', response.text)
    # captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    # elif captcha:
    #     print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Backup and Old files</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ######################################################## Login pages ######################################################

    print ("[#]Checking for Login pages")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" inurl:login&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('There are no results for\s', response.text)
    # captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    # elif captcha:
    #     print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Login pages</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ###################################################### SQL Errors #####################################################

    print ("[#]Checking for SQL errors")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('There are no results for\s', response.text)
    # captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    # elif captcha:
    #     print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible SQL Errors</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ########################################################### Publicly exposed documents ######################################

    print("[#]Checking for Publicly exposed documents ")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('There are no results for\s', response.text)
    # captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    # elif captcha:
    #     print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Publicly Exposed Documents</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")
        f.close()







def process_google():
    
    global f
    
    f.write("<h1>Results from Google</h1>")
    f.write("<br>")
    ############################################### Directory listing #######################################################

    print ("[#]Checking for Directory listing vulnerabilities")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" intitle:index.of&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('\s-\sdid not match any documents.', response.text)
    captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
        
    elif captcha:
        print("[-]Captcha triggered. Please try after some time.\n")


    else:
        print("[+]Registering data into the file.\n")
        
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"> <title>Results from GoogleDorker by nError#NSL</title> </head> <body><br>')
        f.write('<h2>Possible Directory listing</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")


    ########################################################### Config files ################################################

    print ("[#]Checking for Configuration files exposed")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('\s-\sdid not match any documents.', response.text)
    captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    elif captcha:
        print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Configuration files</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ################################################## DB files #######################################################!

    print ("[#]Checking for Database files exposed")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:sql | ext:dbf | ext:mdb&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('\s-\sdid not match any documents.', response.text)
    captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    elif captcha:
        print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Database files</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ###################################################### Log files ####################################################

    print ("[#]Checking for Log files exposed")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:log&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('\s-\sdid not match any documents.', response.text)
    captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    elif captcha:
        print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Log files</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ########################################################## Backup and old files ###########################################

    print ("[#]Checking for Backup and old files")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('\s-\sdid not match any documents.', response.text)
    captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    elif captcha:
        print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Backup and Old files</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ######################################################## Login pages ######################################################

    print ("[#]Checking for Login pages")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" inurl:login&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('\s-\sdid not match any documents.', response.text)
    captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    elif captcha:
        print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Login pages</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ###################################################### SQL Errors #####################################################

    print ("[#]Checking for SQL errors")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('\s-\sdid not match any documents.', response.text)
    captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    elif captcha:
        print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible SQL Errors</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")

    ########################################################### Publicly exposed documents ######################################

    print("[#]Checking for Publicly exposed documents ")

    requesturl = 'https://www.google.com/search?q=site:"' + url + '" ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv&hl=en'
    response = requests.get(requesturl)
    notfound = re.search('\s-\sdid not match any documents.', response.text)
    captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    results = soup.find_all('cite')
    # print(results)

    if notfound:
        print("[-]No results found\n")
    elif captcha:
        print("[-]Captcha triggered. Please try after some time.\n")
    else:
        print("[+]Registering data into the file.\n")
        # f = open(str(url) + ".html", "at")
        # f.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"> <title>Directory Listing</title> </head> <body><br>')
        f.write('<h2>Possible Publicly Exposed Documents</h2>')
        for links in results:
            f.write(str(links) + "<br>")
        f.write("<br>")
        f.write("<br>")
        f.close()

    choice = input("Do you want me to bing the dorks?\n>>")

    if choice == "Y" or choice == "y":
        print("Executing bing...")
        time.sleep(2)
        subprocess.call("clear")
        process_bing()

    else:
        print()

        
process_google()
