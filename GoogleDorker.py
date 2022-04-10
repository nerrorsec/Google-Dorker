#!/usr/bin/env python3
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", dest="domain", help="Domain")
    option = parser.parse_args()
    return option


############# DORKING ############

# Google Dork

def google_dork(domain):
    f = open(str(domain) + '_GoogleDorks.html', 'a')
    f.write(
        f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"> <title>Google Dorks for {domain}</title> </head> <body><br>')

    f.write("<h3>Results from <a href='https://github.com/nerrorsec/GoogleDorker'>GoogleDorker</a> by <a href='https://github.com/nerrorsec'>nerrorsec</a> and <a href='https://github.com/g3nj1z'>g3nj1z</a></h3><br><br>") 

    # File Extensions

    # PHP
    f.write('<h4>File Extensions</h4>')
    url = f"https://www.google.com/search?q=site%3A.{domain}+filetype%3Aphp"
    f.write(f'<a target="_blank" href="{url}">PHP</a>')
    f.write("<br>")
    # ASP
    url = f"https://www.google.com/search?q=site%3A.{domain}+filetype%3Aasp"
    f.write(f'<a target="_blank" href="{url}">ASP</a>')
    f.write("<br>")
    # ASPX
    url = f"https://www.google.com/search?q=site%3A.{domain}+filetype%3Aaspx"
    f.write(f'<a target="_blank" href="{url}">ASPX</a>')
    f.write("<br>")
    # JSP
    url = f"https://www.google.com/search?q=site%3A.{domain}+filetype%3Ajsp"
    f.write(f'<a target="_blank" href="{url}">JSP</a>')
    f.write("<br>")
    # Parameters
    url = f"https://www.google.com/search?q=site%3A.{domain}+inurl%3A%26"
    f.write('<h4>Parameters</h4>')
    f.write(f'<a target="_blank" href="{url}">Parameters</a>')
    f.write("<br>")


    # Important stuffs
    f.write('<h4>Interesting Dorks</h4>')

    # Directory Listing Vulnerabilities
    url1 = f"https://www.google.com/search?q=site%3A.{domain}+intext%3A+%22index+of+%2F%22"
    f.write(f'<a target="_blank" href="{url1}">Index of /</a>')
    f.write("<br>")
    # DB Password
    url2 = f"https://www.google.com/search?q=site%3A.{domain}+db_password+%3D%3D%3D"
    f.write(f'<a target="_blank" href="{url2}">Db_password ===</a>')
    f.write("<br>")
    # Interesting Extensions
    url3 = f"https://www.google.com/search?q=site%3A.{domain}+ext%3Aenv+|+ext%3Alog+|+ext%3Asql+|+ext%3Ayml+|+ext%3Apem+|+ext%3Aini+|+ext%3Alogs+|+ext%3Aibd+|+ext%3Atxt+|+ext%3Aphp.txt+|+ext%3Aold+|+ext%3Akey+|+ext%3Afrm+|+ext%3Abak+|+ext%3Azip+|+ext%3Aswp+|+ext%3Aconf+|+ext%3Adb+|+ext%3Aconfig+|+ext%3Aovpn+|+ext%3Asvn+|+ext%3Agit+|+ext%3Acfg+|+ext%3Aexs+|+ext%3Adbf+|+ext%3Amdb+ext%3Apem+ext%3Apub+ext%3Ayaml+ext%3Azip+ext%3Aasc+ext%3Axls+ext%3Axlsx"
    f.write(f'<a target="_blank" href="{url3}">Interesting Extensions</a>')
    f.write("<br>")
    # Publicly Exposed Documents
    url4 = f"https://www.google.com/search?q=site%3A.{domain}+ext%3Adoc+%7C+ext%3Adocx+%7C+ext%3Aodt+%7C+ext%3Artf+%7C+ext%3Asxw+%7C+ext%3Apsw+%7C+ext%3Appt+%7C+ext%3Apptx&rlz=1C1CHBF_enMY893MY893&oq=site%3Ahttps%3A%2F%2Fwww.atg.se+ext%3Adoc+%7C+ext%3Adocx+%7C+ext%3Aodt+%7C+ext%3Artf+%7C+ext%3Asxw+%7C+ext%3Apsw+%7C+ext%3Appt+%7C+ext%3Apptx"
    f.write(f'<a target="_blank" href="{url4}">Publicly Exposed Documents</a>')
    f.write("<br>")
    # Configuration Files Exposed
    url5 = f"https://www.google.com/search?q=site%3A.{domain}+ext%3Axml+%7C+ext%3Aconf+%7C+ext%3Acnf+%7C+ext%3Areg+%7C+ext%3Ainf+%7C+ext%3Ardp+%7C+ext%3Acfg+%7C+ext%3Atxt+%7C+ext%3Aora+%7C+ext%3Aini+%7C+ext%3Aenv"
    f.write(f'<a target="_blank" href="{url5}">Configuration Files Exposed</a>')
    f.write("<br>")
    ## Database Files Exposed
    url6 = f"https://www.google.com/search?q=site%3A.{domain}+ext%3Asql+%7C+ext%3Adbf+%7C+ext%3Amdb"
    f.write(f'<a target="_blank" href="{url6}">Database Files Exposed</a>')
    f.write("<br>")
    ## Backup and Old Files
    url7 = f"https://www.google.com/search?q=site%3A.{domain}+ext%3Abkf+%7C+ext%3Abkp+%7C+ext%3Abak+%7C+ext%3Aold+%7C+ext%3Abackup"
    f.write(f'<a target="_blank" href="{url7}">Backup and Old Files</a>')
    f.write("<br>") 
    ## Credentials and Password
    url8 = f"https://www.google.com/search?q=site%3A.{domain}+password+%7C+credential+%7C+username+filetype%3Alog"
    f.write(f'<a target="_blank" href="{url8}">Credentials and Password</a>')
    f.write("<br>") 
    ## Confidential xls, csv, doc, txt 
    url9 = f"https://www.google.com/search?q=site%3A.{domain}+not+for+distribution+%7C+confidential+%7C+“employee+only”+%7C+proprietary+%7C+top+secret+%7C+classified+%7C+trade+secret+%7C+internal+%7C+private+filetype%3Axls+%7C+private+filetype%3Acsv+%7C+private+filetype%3Adoc+%7C+private+filetype%3Atxt"
    f.write(f'<a target="_blank" href="{url9}">Confidential xls, csv, doc, txt</a>')
    f.write("<br>") 
    ## Confidential Employee log
    url10 = f"https://www.google.com/search?q=site%3A.{domain}+not+for+distribution+%7C+confidential+%7C+“employee+only”+%7C+proprietary+%7C+top+secret+%7C+classified+%7C+trade+secret+%7C+internal+%7C+private+%7C+WS_FTP+%7C+ws_ftp+%7C+log+%7C+LOG+filetype%3Alog&rlz=1C1CHBF_enMY893MY893&oq=inurl%3A.gov+not+for+distribution+%7C+confidential+%7C+“employee+only”+%7C+proprietary+%7C+top+secret+%7C+classified+%7C+trade+secret+%7C+internal+%7C+private+%7C+WS_FTP+%7C+ws_ftp+%7C+log+%7C+LOG+filetype%3Alog"
    f.write(f'<a target="_blank" href="{url10}">Confidential log</a>')
    f.write("<br>") 

    # More
    f.write('<h4>More</h4>')

    # Possible Login Pages
    url11 = f"https://www.google.com/search?q=site%3A.{domain}+inurl%3Asignin+%7C+intitle%3ALogin+%7C+intitle%3A"'sign+in'"+%7C+inurl%3Aauth"
    f.write(f'<a target="_blank" href="{url11}">Possible Login Pages</a>')
    f.write("<br>")
    # Possible Signup Pages
    url12 = f"https://www.google.com/search?q=site%3A.{domain}+inurl%3Aregister+%7C+intitle%3ASignup"
    f.write(f'<a target="_blank" href="{url12}">Possible Signup Pages</a>')
    f.write("<br>")
    #Possible SQL Errors
    url13 = f"https://www.google.com/search?q=site:.{domain}+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22&hl=en"
    f.write(f'<a target="_blank" href="{url13}">Possible SQL Errors</a>')
    f.write("<br>")
    # phpinfo()
    url14 = f'https://www.google.com/search?q=site:.{domain}+ext:php+intitle:phpinfo+"published+by+the+PHP+Group"'
    f.write(f'<a target="_blank" href="{url14}">phpinfo();</a>')
    f.write("<br>")
    f.close()

# Vendork 

def vendork(domain):
    k = f'https://www.{domain}'
    ke = re.findall('\.\w.*\.', str(k))
    key = re.findall('\w.*\w', str(ke[0]))
    keyword = str(key[0])

    f = open(str(keyword) + '_VenDorks.html', 'a')
    f.write(
        f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"> <title>Vendor Dorks for {keyword}</title> </head> <body><br>')
    f.write("<h3>Results from <a href='https://github.com/nerrorsec/GoogleDorker'>GoogleDorker</a> by <a href='https://github.com/nerrorsec'>nerrorsec</a> and <a href='https://github.com/g3nj1z'>g3nj1z</a></h3><br><br>")
    vendors = ["*.atlassian.net", "bitbucket.org", "bitpaste.app", "codebeautify.org", "codepad.co", "codepen.io", "codepad.org", "coggle.it", "codeshare.io", "dotnetfiddle.net", 
               "dpaste.org", "dpaste.com", "github.com", "gitter.im", "heypasteit.com", "hastebin.com", "ideone.com", "ide.geeksforgeeks.org", "jsfiddle.net", "justpaste.it",
               "jsdelivr.net", "jsitor.com", "libraries.io", "npmjs.com", "npm.runit.com", "papaly.com", "pastebin.com", "paste.debian.net", "paste.org", "paste2.org", "pastehtml.com", "phpfiddle.org", "prezi.com",
               "repl.it", "scribd.com", "snipplr.com", "snipt.net", "slexy.org", "textsnip.com", "trello.com"]
    for x in vendors:
        url = f"https://www.google.com/search?q=site%3A%22{x}%22+%22{keyword}%22"
        f.write(f'<a target="_blank" href="{url}">{x}</a>')
        f.write("<br>")

    inurl_vendors = ["gitlab"]
    for x in inurl_vendors:
        url = f"https://www.google.com/search?q=inurl%3A%22{x}%22+%22{keyword}%22"
        f.write(f'<a target="_blank" href="{url}">{x}</a>')
        f.write("<br>")

    f.close()

options = get_arguments()
if options.domain and re.match("^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$", options.domain):
    google_dork(options.domain)
    vendork(options.domain)
    print("\n[+] Success. Please check the newly created files.")
else:
    print("\n[-] Usage: python3 GoogleDorker.py -d example.com")
