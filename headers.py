import requests
import pyfiglet
import datetime
import os

print(
"""
\u001b[31m

                                WWWWWWWWWWWWWWWWWWWWWNXKK0OOkkkkkOO0KXNWWWWWWWWWWWWWWWWWWWWW
                                WWWWWWWWWWWWWWWWNX0kdlc:;,,,,,,,,,,;:cldxOKNWWWWWWWWWWWWWWWW
                                WWWWWWWWWWWWWNKkoc;,,;cldxxkkkkkkxo;'''',,:lx0NWWWWWWWWWWWWW
                                WWWWWWWWWWWXOo:,,:oxOKXNWWWWWWWWWWXo,',,'''',;lkKNWWWWWWWWWW
                                WWWWWWWWWXkc,,,ckKNWWWWWWWWWWWWWWWNO:'','',,',',:xKNWWWWWWWW
                                WWWWWWWNOl,''',cONWWWWWWWWWWWWWWWWWNOl;,'','',''',:xXWWWWWWW
                                WWWWWWKd;,''''''cOWWWWWWWWWWWWWWWWWWWX0dc,,''',''',,l0NWWWWW
                                WWWWW0l,,,,'',,';kNWWWWWWWWWWWWWWWWWWWWWXko;,''',',',cONWWWW
                                WWWWKl,','',,;coOXWWWWWWWWWWWWWWWWWWWWWWWWN0d:,',,:c;,:ONWWW
                                WWWXo,'''',:xKXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNO:,ckXKd;,c0WWW
                                WWNk;',''',oXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNx:xNWWKl,,dXWW
                                WWKl,,''',,oXWWWWWWWWWWWWWWWNNNNWWWWWWWWWWWWWWOcoXWWNk;':OWW
                                WWO:',''',,cONWWWWWWWWWWWWWWOllokKNWWWWWWWWWWNk:;dXWWKl,;xNW
                                WNk;'''','',oKWWWWWWWWWWWWWW0c'',:lx0NWWWWWWXx:,,,ckXXo,,dXW
                                WNk;''',;cdOXNWWWWWWWWWWWWWWXo,,''',;lx0XWWN0l,,''',lko,,dXW
                                WNk:',cx0XWWWWWWWWWWWWWWWWWWNkc;'''''',;cdOXNXOdc;,',::,,dNW
                                WW0c';xNWWNKkxddOXWWWWWWWWWWWKkl,,,''''''',cokKNX0xc;,,':kNW
                                WWNd,,l0WNk:,''',lkXNWWWWWWWWNKd,''''''''''',,:okKNX0xl:oKWW
                                WWW0l,,dKk:,'',',,,:oxkKNWWWWWNO:''''''''',''''',:lx0XNKXWWW
                                WWWNO:,;c;''','',,','':kNWWWWWWXo,,,,''','''''''''',;ld0XWWW
                                WWWWNO:,'','',,''',,;lONWWWWWWWNx;',,'',''''''''''',,,;cxXWW
                                WWWWWN0c,''''''',cxOKNWWWWWWWWWW0c'','',''''''';ldxkkO0KXNWW
                                WWWWWWWKd;,'','',dNWWWWWWWWWWWWWXd,''','''',''':kNWWWWWWWWWW
                                WWWWWWWWN0o;,,,,'c0WWWWWWWWWWWWWNO:''''',;,,''',:xXWWWWWWWWW
                                WWWWWWWWWWN0d:,'';d0XNWWWWWWWWWWWKl,,,',oOkl,'''';oKWWWWWWWW
                                WWWWWWWWWWWWNKko:,,;:ldxO00KKKKXWNx;',;xXWWKd;'''',cONWWWWWW
                                WWWWWWWWWWWWWWWNXOxoc;,,,,;;:::oKW0c,:kNWWWWNk:,',',:kNWWWWW
                                WWWWWWWWWWWWWWWWWWWNXK0kxddooooxKWXxo0NWWWWWWN0o,''',dNWWWWW
                                WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNWWWWWWWWWWXkollxKWWWWWW
                                WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNWWWWWWWW 
\u001b[34m
         _______ ______             _______ _______ ______  _______ _______ _______    _______ _______ _______ _       _       _______ _______ 
|\     /(  ____ (  ___ \   |\     /(  ____ (  ___  |  __  \(  ____ (  ____ |  ____ \  (  ____ (  ____ (  ___  | (    /( (    /(  ____ (  ____ )
| )   ( | (    \/ (   ) )  | )   ( | (    \/ (   ) | (  \  ) (    \/ (    )| (    \/  | (    \/ (    \/ (   ) |  \  ( |  \  ( | (    \/ (    )|
| | _ | | (__   | (__/ /   | (___) | (__   | (___) | |   ) | (__   | (____)| (_____   | (_____| |     | (___) |   \ | |   \ | | (__   | (____)|
| |( )| |  __)  |  __ (    |  ___  |  __)  |  ___  | |   | |  __)  |     __|_____  )  (_____  ) |     |  ___  | (\ \) | (\ \) |  __)  |     __)
| || || | (     | (  \ \   | (   ) | (     | (   ) | |   ) | (     | (\ (        ) |        ) | |     | (   ) | | \   | | \   | (     | (\ (   
| () () | (____/\ )___) )  | )   ( | (____/\ )   ( | (__/  ) (____/\ ) \ \_/\____) |  /\____) | (____/\ )   ( | )  \  | )  \  | (____/\ ) \ \__
(_______|_______// \___/   |/     \(_______//     \(______/(_______//   \__|_______)  \_______|_______//     \|/    )_)/    )_|_______//   \__/                                                                                                                      
 \u001b[34m                                                                                                                                                                      
"""
)
print("========"*20)
print("\n")
print("1.Scan target to HTTP headers")
print("2.HTTP Scan Results")
print("\n")
print("========"*20)

class scanheaders:
     def __init__(self,url):
        self.url     = url
        response     = requests.get(url)
        self.headers = response.headers
        self.cookies = response.cookies

     def xss(self):
        try:
            if self.headers["x-xss-protection"]:
                print("[+]"," x-xss=protection : \u001b[32mPass\u001b[32m")
        except KeyError:
                print("[-]"," x-xss=protection : \u001b[31mFail!\u001b[31m")

     def nosniff(self):
        try:
            if self.headers["x-Content-Type-Option"].lower() == "nosniff":
                print("[+]","x-Content-Type-Option : \u001b[32mPass\u001b[32m")
            else:
                 print("[-]","x-Content-Type-Option headers not set correctly  : \u001b[31mFail\u001b[31m")
        except:
            print("[-]","x-Content-Type-Option headers not set present  : \u001b[31mFail!\u001b[31m")

     def xframe(self):
       try:
            if "deny" in self.headers["X-Frame-Options"].lower():
               print("[+] X-Frame-Options :  \u001b[32mpass\u001b[32m")
            elif "sameorigin" in self.headers["X-Frame-Options"].lower():
                print("[+] X-Frame-Options :  \u001b[32mpass\u001b[32m")
            else:
              print("[-]  X-Frame-Options header not set correctly  :  \u001b[31mfail!\u001b[31m")
       except KeyError:
            print("[-]  X-Frame-Options header not present  :  \u001b[31mfail!\u001b[31m")

     def hsts(self):
        try:
          if self.headers["Strict-Transport-Security"]:
                print("[+]  Strict-Transport-Security  :  \u001b[32mpass\u001b[32m")
        except KeyError:
             print("[-]   Strict-Transport-Security header not present  : \u001b[31mfail!\u001b[31m")

     def policy(self):
         try:
            if self.headersFail ["Content-Security-Policy"]:
               print("[+]   Content-Security-Policy   :  \u001b[32mpass\u001b[32m")
         except KeyError:
               print("[-]   Content-Security-Policy header not present  :  \u001b[31mfail!\u001b[31m")

     def secure(self, cookie):
         if cookie.secure:
            print("[+]  Secure  :  \u001b[32mpass\u001b[32m")
         else:
            print("[-]  Secure attribute not set  :  \u001b[31mfail!\u001b[31m")

     def httponly(self, cookie):
        if cookie.has_nonstandard_attr('httponly') or cookie.has_nonstandard_attr('HttpOnly'):
            print("[+]  HttpOnly  :  \u001b[32mpass\u001b[32m")
        else:
            print("[-]  HttpOnly attribute not set  :  \u001b[31mfail!\u001b[31m")


if __name__ == "__main__":
    print("\n")
    input = str(input(" web site link past here : "))
    date = datetime.datetime.now()
    print("\n")
    print(f"Scaning time : ",date)
    print(f"Scaning website : ",input)
    print("\n")
    target = scanheaders(input)

    for key in target.headers:
      print(key, ":", target.headers[key])
      print()
      print("\n")
     
    target.xss()
    target.nosniff()
    target.xframe()
    target.hsts()
    target.policy()
   
    for cookie in target.cookies:
        print("\u001b[34mSet-Cookie:\u001b[34m")
        target.secure(cookie)
        target.httponly(cookie)

