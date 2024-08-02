import random

from colorama import Fore
import pyfiglet

print(Fore.LIGHTYELLOW_EX + pyfiglet.figlet_format("Baza  Danych"))

print(Fore.LIGHTBLUE_EX + "Informcje o Robercie Kaczynskim:" + Fore.RESET)
informacje = {'name': 'Robert Kaczynski',
              'ip address': '39.352.35.467',
              'home address': 'Kaczyńska 12B'}
print (informacje)

firmy = ['Elon Mózg', 'Meta']
firma = random.choice(firmy)


def sell(firma):
    """Sprzedaje informacje o Robercie Kaczyńskim"""
    print('Sprzedano informacje o ' + Fore.LIGHTRED_EX + 'Robercie Kaczyńskim' + Fore.RESET + ' do ' + Fore.LIGHTCYAN_EX + firma)

sell(firma)
