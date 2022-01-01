# MADE BY AVALANCHE | Avalanche#2630

import os, time

os.system("pip install selenium==3.141.0")
os.system("clear")

from webbot import Browser

class WebEagle:
      BrowsingAs = ""
      def Browser(proxy: str = None):
                 if proxy == None:
                    WebEagle.BrowsingAs = Browser()
                 else:
                    try:
                        WebEagle.BrowingAs = Browser(proxy = proxy)
                    except:
                        print(' Bad Proxy | {} | WebEagle'.format(proxy))
                        WebEagle.BrowsingAs = Browser() 

      def get(url: str, delay: int = None):
          try: 
              if WebEagle.BrowsingAs == "":
                 exit(print(" Insufficient Browsing Data | WebEagle"))
              else:
                 if "https://" or "http://" in url:
                    WebEagle.BrowsingAs.go_to(url)
                 else:
                    print("Cannot GET Invalid Website | {} | WebEagle".format(url))
          except Exception as E:
               exit(print(E))

WebEagle.Browser()
WebEagle.get("https://canary.discord.com/login")

WebEagle.BrowsingAs.type(input("[$] Enter Account EMAIL : "), xpath = "/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input")
WebEagle.BrowsingAs.type(input("[$] Enter Account PASSWORD : "), xpath = "/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input")

print("[$] READY ")
WebEagle.BrowsingAs.type(WebEagle.BrowsingAs.Key.ENTER)
time.sleep(5)

WebEagle.get("https://top.gg/bot/270904126974590976/vote")
input("[$] LOGIN TO TOP.GG | PRESS ENTER WHEN READY :: ")

time.sleep(15)
WebEagle.BrowsingAs.click(xpath = "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/main/div[1]/div/div[2]/button")

while True:
      time.sleep(43200)
      WebEagle.get("https://top.gg/bot/270904126974590976/vote")

      time.sleep(15)
      WebEagle.BrowsingAs.click(xpath = "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/main/div[1]/div/div[2]/button")
