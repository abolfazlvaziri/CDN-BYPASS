import socket 
import sys
import os
from colorama import Fore as color
from time import sleep


bold = '\033[1m'
endbold = '\033[0m'

def banner():
    print(bold+color.RED+'''
        
         # #       #             # # #       
        #   #       #           #  #  #      CDN BYPASS
       #     #       #         #   #   #      
      #       #       #       #    #    #    
     #         #       #     #     #     #   
    #           #       #   #      #      #  
   #             #       # #       #       # 

     '''+endbold)

    print(bold+color.WHITE+'''
    
         -----------------------
       ⚒  SUBDOMAIN ENUMERATION  ⚒    
            ⚒  CDN BYPASS  ⚒ 
         -----------------------
         
     '''+endbold)  
    sleep(1)

os.system('clear')
banner()



def CDN():
    try:
        subdomain = [
            'www', 'mail', 'webmail', 'blog', 'news', 'shop', 'store', 'forum',
            'support', 'help', 'dev', 'test', 'staging', 'demo', 'beta', 'stage',
            'app', 'api', 'cdn', 'static', 'media', 'images', 'video', 'music',
            'chat', 'stats', 'wiki', 'docs', 'files', 'download', 'portal', 'crm',
            'admin', 'dashboard', 'panel', 'login', 'auth', 'register', 'signup',
            'subscribe', 'unsubscribe', 'feedback', 'contact', 'about', 'career',
            'jobs', 'partners', 'affiliate', 'investor', 'blog', 'press', 'newsroom',
            'events', 'conference', 'summit', 'forum', 'community', 'network', 'marketplace',
            'store', 'shop', 'auction', 'deal', 'offer', 'sale', 'discount', 'coupon',
            'gift', 'reward', 'cashback', 'charity', 'donate', 'fund', 'sponsor', 'survey',
            'quiz', 'poll', 'contest', 'game', 'gambling', 'lottery', 'bet', 'casino', 'poker',
            'sport', 'fitness', 'health', 'nutrition', 'diet', 'recipe', 'cooking', 'restaurant',
             'food'
             ]

        URL = input("Please Enter Target:")

        if URL == "":
            try:
                print("Please Enter Address :)")
                sys.exit()
            except:
                return
        for sub in subdomain:
            try:
                http = str(sub) + "." + str(URL)
                bypass = socket.gethostbyname(str(http))
                print(" [+] CDN Bypass " + str(bypass) + ' | ' + str(http))
            except:
                pass
        try:
            input("\n [*] Finish (Press Enter...) ")
        except:
            print("")
            sys.exit()
    except:
        print("")

CDN()