import json
import os
import colorama
from colorama.initialise import colorama_text
try:
    from colorama import Fore, Style
except:
    os.system("python -m pip install colorama")
    try:
        from colorama import Fore, Style
    except:
        print(f"[ERROR] Couldn't Import Needed Librarys, press [ENTER] to exit"); input(); exit()

err = f"[{Fore.RED}-{Style.RESET_ALL}]"
out = f"[{Fore.GREEN}:{Style.RESET_ALL}]"
inp = f"[{Fore.MAGENTA}>{Style.RESET_ALL}]"
deb = f"[{Fore.CYAN}${Style.RESET_ALL}]"
inf = f"[{Fore.YELLOW}i{Style.RESET_ALL}]"
finish = f"press [{Fore.YELLOW}ENTER{Style.RESET_ALL}] to return"
finishe = f"press [{Fore.YELLOW}ENTER{Style.RESET_ALL}] to exit"
banner = '''
 ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗      ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗
██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝
██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝    ██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗
██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗    ██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║
╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝    ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝'''

def colorinp():
    global ic
    global debug
    debug = None

    if debug == None:
        ic = input(f"\n{inp} Programing Language [d for debug]: ")
    else:
        ic = input(f"\n{inp} Programing Language: ")

    if ic == "d" and debug == None:
        debug = True; print(f"{deb} Debug {Fore.GREEN}On{Style.RESET_ALL}")
        print(f"{finish}"); input(); colorinp()
    else:
        debug = False; print(f"{deb} Debug {Fore.RED}Off{Style.RESET_ALL}\n")

def getlist():
    li = input(f"\n{inp} List 1 or 2 [1/2]: ")
    if int(li) == 1:
        colorinp()
        colors1()
    elif int(li) == 2:
        colorinp()
        colors2()
    
f = open("./githubColors.json")
getcolors = json.load(f); f.close()
f = open("./githubColors-2.json")
getcolors1 = json.load(f); f.close()

def screen():
    os.system("cls;clear"); print(banner)
    print(f"{inf} List 2 Includes GitHub-Topic URL and Colorcode\n{inf} List 1 only includes Colorcde")
    getlist()

def colors1():
    try:
        color = getcolors.get(f'{ic}')
        if color == None:
            try:
                if debug == True:
                    print(f"{deb} Capitalzing")
                color = getcolors.get(f'{ic.capitalize}')
                if color != None:
                    if debug == True:
                        print(f"{deb} Found Color")
                    print(f"{out} Colorcode: {color} \n{finishe} "); input(); exit()
                else:
                    print(f"{err} Couldn'f find Language \n{err} Try Writing the Full Language Name or Using List 1\n{finishe}"); input(); exit()
            except:
                print(f"{err} Couldn'f find Language \n{err} Try Writing the Full Language Name or Using List 1\n{finishe}"); input(); exit()
        else:
            print(f"{out} Colorcode: {color} \n{finishe}"); input(); exit()
    except Exception as e:
        print(f"{err} {e} \n{finishe}"); input(); exit()

def colors2():
    try:
        getcolor = getcolors1.get(f'{ic}')
        color = getcolor.get("color")
        url = getcolor.get("url")
        if color == None:
            try:
                if debug == True:
                    print(f"{deb} Capitalzing")
                color = getcolors1.get(f'{ic.capitalize}')
                if color != None:
                    if debug == True:
                        print(f"{deb} Found Color")
                    print(f"{out} Colorcode: {color}\n{out} Topic-Url: {url} \n{finishe} "); input(); exit()
                else:
                    print(f"{err} Couldn'f find Language \n{err} Try Writing the Full Language Name or Using List 1\n{finishe}"); input(); exit()
            except:
                print(f"{err} Couldn'f find Language \n{err} Try Writing the Full Language Name or Using List 1\n{finishe}"); input(); exit()
        else:
            print(f"{out} Colorcode: {color}\n{out} Topic-Url: {url} \n{finishe}"); input(); exit()
    except Exception as e:
        print(f"{err} {e} \n{finishe}"); input(); exit()
screen()
