import colorama
from colorama import init, Fore, Back, Style
import pyfiglet

colorama.init()

print(Fore.CYAN + "Hello Wiktor")
print(Back.RED + Fore.LIGHTWHITE_EX + "POLSKA" + Back.RESET)

caption = pyfiglet.figlet_format("Wiktor")
print(caption)
