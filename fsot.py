#coded by MR.Puxonz
#Python3
#Free Online Phone Number
import requests
import os
import sys
from bs4 import BeautifulSoup

c = requests.Session()
def main():
   os.system("clear")
   print ("""\033[35m    ___________ ____  ______
   / ____/ ___// __ \/_  __/  \033[33m|\033[32mAuth \033[31m: \033[37mPuxonz\033[35m
  / /_   \__ \/ / / / / /     \033[33m|\033[32mTeam \033[31m: \033[37mBlackCoderCrush\033[35m
 / __/  ___/ / /_/ / / /
/_/    /____/\____/ /_/ \033[33mv 0.1
\033[32m  Free Sms Online Tool
   """)
   url = "https://www.receivesmsonline.net"
   try:
       r = c.get(url)
       soup = BeautifulSoup(r.content, "html.parser")
       t = soup.find_all("div", class_="col-md-5")
       no = -3
       for i in t:
           a = i.findChildren("h2")
           no += 1
           for u in a:
                print ("\033[33m[\033[31m"+str(no)+"\033[33m]\033[32m"+u.text)
       pilih()
   except requests.exceptions.ConnectionError:
       print ("\033[31mJaringan Buruk")
def get_link(n):
   url = "https://www.receivesmsonline.net"
   try:
       r = c.get(url)
       soup = BeautifulSoup(r.content, "html.parser")
       t = soup.find_all("div", class_="col-md-5")
       no = -3
       for i in t:
           no += 1
           if no == n:
               for u in i.findChildren("a"):
                   global link
                   link = u.get("href")
   except requests.exceptions.ConnectionError:
       print ("\033[31mJaringan Buruk")
def pilih():
   pil = input("\n\033[33mPilih Nomor \033[31m: \033[35m")
   if pil == "-2" or "0":
      print ("\033[31mError")
      sys.exit()
   get_link(int(pil))
   show()
def show():
   try:
        url = link
        r = c.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        main_table = soup.find_all("table", class_="table table-striped table-bordered")
        right_table = soup.find("table", class_="table table-striped table-bordered")
        A = []
        B = []
        C = []
        for row in right_table.find_all("tr"):
             cells = row.find_all("td")
             if len(cells)==3:
                  A.append(cells[0].find(text=True))
                  B.append(cells[1].find(text=True))
                  C.append(cells[2].find(text=True))
        print ("\n\033[33m[\033[31m+\033[33m]\033[32mMessages\033[33m[\033[31m+\033[33m]\n")
        no = 0
        hm = -1
        for i in C:
            no += 1
            hm += 1
            print ("\033[33m[\033[31m"+str(no)+"\033[33m]\033[35m",str(i)+" ("+B[hm]+")")
        ju = input("\n\033[33m[\033[32mKembali\033[33m]")
        main()
   except requests.exceptions.ConnectionError:
        print ("\033[31mJaringan Buruk")

main()
