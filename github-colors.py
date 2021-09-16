import json
import os
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
finish = f"press [{Fore.YELLOW}ENTER{Style.RESET_ALL}] to exit"

banner = '''
 ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗      ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗
██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝
██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝    ██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗
██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗    ██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║
╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝    ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
'''

f = open("./githubColors.json")
colors = json.load(f)
f.close()

os.system("cls;clear")
print(banner)
ic = input(f"{inp} Programing Language: ")
try:
    color = colors.get(f'{ic}')
    if color == None:
        print(f"{err} Couldn'f find Language \n{err} Try Writing the Full Language Name \n{finish}"); input(); exit()
    else:
        print(f"{out} Colorcode: {color} \n{finish}"); input(); exit()
except Exception as e:
    print(f"{err} {e}, {finish}"); input(); exit()
