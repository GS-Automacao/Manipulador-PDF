from configs.utils.update_functions import check_update
from configs.utils.menu_functions import main_hub
import ctypes
import os
import sys
ctypes.windll.kernel32.SetConsoleTitleW("Manipulador de PDF")



VERSION: str = 'v1.4.1'


def run():
    print('Manipulador de PDFs')
    print(VERSION)
    check_update(VERSION)  # Verifica se há atualizações.
    main_hub()  # inicia o menu.


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print(e)
        input()
