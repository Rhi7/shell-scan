#!/usr/bin/python3
# Code by PosiX

import urllib.request
import argparse
import sys
import time

class ZeroScann():
    # initialize
    def __init__(self):
        self.main()
        
    def main(self):
        parser = argparse.ArgumentParser(prog="shell.py",
                                         description="Find web shell"
                                         )
        parser.add_argument("-u", dest="domain", help="your url")
        parser.add_argument("-w", dest="wordlist", help="your wordlsit")
        args = parser.parse_args()
        if not args.domain:
            sys.exit("\033[36musage: shell.py -u example.com -w wordlist.txt")
        if not args.wordlist:
            sys.exit("\033[36musage: shell.py -u example.com -w wordlist.txt")
            
        # handle url website
        site = args.domain
        print("\033[96m[!] \033[0mConnection, wait a sec!\n")
        time.sleep(3)
        if not site.startswith("http://"):
            site = "http://"+site
        if not site.endswith("/"):
            site = site+"/"
        # load wordlist
        try:
            asu = args.wordlist
            wlist = open(asu, "r")
            wordlist = wlist.readlines()
        except FileNotFound as e:
            print("\033[91mUpss, Wordlist Not Found!\033[0m")
        finally:
            try:
                wlist.close()
            except:
                print("\033[91mWordlist Can\'t Close!\033[0m")
        # loop wordlist with site address
        for psx in wordlist:
            psx = psx.replace("\n", "")
            url = site+psx
            req = urllib.request.Request(url)
            time.sleep(0.1)
            try:
                response = urllib.request.urlopen(req)
                print("\033[93m[\033[34m{0}\033[93m]".format(time.strftime("%H:%M:%S")),"\033[92minfo : ","\033[92m/"+psx,"✓")
                again = input("\033[93m[\033[34m{0}\033[93m] \033[96mcontinue to scann (y/n) ".format(time.strftime("%H:%M:%S")))
                if again == "y":
                    continue
                else:
                    print("\n\033[96m[!] \033[0mExit Program, wait!")
                    time.sleep(3)
                    print("\033[96m[!] \033[0mDone!\033[0m")
                    exit()
            except urllib.error.HTTPError as e:
                print("\033[93m[\033[34m{0}\033[93m]".format(time.strftime("%H:%M:%S")),"\033[91merror: ","\033[0m/"+psx)
        print("\n\033[96m[!] \033[0mScann Complete!")

    def banner():
        # banner display
        psx = """\033[33m
                    ___
                  .'   '.
                 :       :
                 | _   _ |
              .-.|(\033[91m0\033[93m)_(\033[91m0\033[93m)|.-.
             ( ( | .--.  | ) )
              '-/ (    )  \-'
               /   '--'    \\
               \ `\033[91m"===="\033[93m`  /
                '\       /'
                 '\     /'
                 _/'-.-'\_
            _..:;\._/v\_./:;.._
          .'/;:;:;\ /^\ /;:;:;\\'.
         / /;:;:;:;\| |/:;:;:;:\ \\
        / /;:;:;:;:;\_/:;:;:;:;:\ \\ \033[91m
 # ================================== #
 # Shell Scanner                      #
 # Code by PosiX                      #\033[0m
 # Twitter: @posiX                    #
 # http://maqlo-heker.blogspot.com    #
 # ================================== #
              """
        return psx
    print(banner())
                
if __name__ == '__main__':
    ZeroScann()