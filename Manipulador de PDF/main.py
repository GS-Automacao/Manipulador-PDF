from configs.utils.update_functions import check_update
from configs.utils.menu_functions import main_hub
import ctypes
import os
import sys
ctypes.windll.kernel32.SetConsoleTitleW("Manipulador de PDF")


if getattr(sys, 'frozen', False):
    # Caminho da pasta onde o executável está
    ROOT_DIR = os.path.dirname(sys.executable)
else:
    # Caminho da pasta onde o script .py está
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


VERSION: str = 'v1.3.0'


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
