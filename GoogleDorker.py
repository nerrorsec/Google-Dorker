#!/usr/bin/env python3
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", dest="domain", help="Domain")
    option = parser.parse_args()
    return option


############# DORKING ############
def google_dork(domain):
    f = open(str(domain) + '_GoogleDorks.html', 'a')
    f.write(
        f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"> <title>Google Dorks for {domain}</title> </head> <body><br>')

    f.write("<h3>Results from <a href='https://github.com/nerrorsec/GoogleDorker'>GoogleDorker</a> by <a href='https://github.com/nerrorsec'>nerrorsec</a></h3><br><br>")

    # file extensions
    f.write('<h4>File Extensions</h4>')
    url = f"https://www.google.com/search?q=site%3A.{domain}+filetype%3Aphp"
    f.write(f'<a target="_blank" href="{url}">PHP</a>')
    f.write("<br>")

    url = f"https://www.google.com/search?q=site%3A.{domain}+filetype%3Aasp"
    f.write(f'<a target="_blank" href="{url}">ASP</a>')
    f.write("<br>")

    url = f"https://www.google.com/search?q=site%3A.{domain}+filetype%3Aaspx"
    f.write(f'<a target="_blank" href="{url}">ASPX</a>')
    f.write("<br>")

    url = f"https://www.google.com/search?q=site%3A.{domain}+filetype%3Ajsp"
    f.write(f'<a target="_blank" href="{url}">JSP</a>')
    f.write("<br>")

    # parameters
    url = f"https://www.google.com/search?q=site%3A.{domain}+inurl%3A%26"
    f.write('<h4>Parameters</h4>')
    f.write(f'<a target="_blank" href="{url}">Parameters</a>')
    f.write("<br>")

    # Important stuffs
    f.write('<h4>Interesting Dorks</h4>')

    url1 = f"https://www.google.com/search?q=site%3A.{domain}+intext%3A+%22index+of+%2F%22"
    f.write(f'<a target="_blank" href="{url1}">Index of /</a>')
    f.write("<br>")

    url2 = f"https://www.google.com/search?q=site%3A.{domain}+db_password+%3D%3D%3D"
    f.write(f'<a target="_blank" href="{url2}">db_password ===</a>')
    f.write("<br>")

    url3 = f"https://www.google.com/search?q=site%3A.{domain}+ext%3Aenv+|+ext%3Alog+|+ext%3Asql+|+ext%3Ayml+|+ext%3Apem+|+ext%3Aini+|+ext%3Alogs+|+ext%3Aibd+|+ext%3Atxt+|+ext%3Aphp.txt+|+ext%3Aold+|+ext%3Akey+|+ext%3Afrm+|+ext%3Abak+|+ext%3Azip+|+ext%3Aswp+|+ext%3Aconf+|+ext%3Adb+|+ext%3Aconfig+|+ext%3Aovpn+|+ext%3Asvn+|+ext%3Agit+|+ext%3Acfg+|+ext%3Aexs+|+ext%3Adbf+|+ext%3Amdb+ext%3Apem+ext%3Apub+ext%3Ayaml+ext%3Azip+ext%3Aasc+ext%3Axls+ext%3Axlsx"
    f.write(f'<a target="_blank" href="{url3}">Interesting extensions</a>')
    f.write("<br>")

    # More
    f.write('<h4>More</h4>')

    url4 = f"https://www.google.com/search?q=site%3A.{domain}+inurl%3Alogin"
    f.write(f'<a target="_blank" href="{url4}">Possible Login Pages</a>')
    f.write("<br>")

    url5 = f"https://www.google.com/search?q=site:.{domain}+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22&hl=en"
    f.write(f'<a target="_blank" href="{url5}">Possible SQL Errors</a>')
    f.write("<br>")

    url6 = f'https://www.google.com/search?q=site:.{domain}+ext:php+intitle:phpinfo+"published+by+the+PHP+Group"'
    f.write(f'<a target="_blank" href="{url6}">phpinfo();</a>')
    f.write("<br>")
    f.close()

def vendork(domain):
    k = f'https://www.{domain}'
    ke = re.findall('\.\w.*\.', str(k))
    key = re.findall('\w.*\w', str(ke[0]))
    keyword = str(key[0])

    f = open(str(keyword) + '_VenDorks.html', 'a')
    f.write(
        f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"> <title>Vendor Dorks for {keyword}</title> </head> <body><br>')
    f.write("<h3>Results from <a href='https://github.com/nerrorsec/GoogleDorker'>GoogleDorker</a> by <a href='https://github.com/nerrorsec'>nerrorsec</a></h3><br><br>")
    vendors = ["*.atlassian.net", "bitbucket.org", "codepad.co", "codepen.io", "coggle.it", "github.com", "gitter.im",
               "jsdelivr.net", "libraries.io", "npmjs.com", "npm.runit.com", "papaly.com", "pastebin.com", "prezi.com",
               "repl.it", "scribd.com", "trello.com"]
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
