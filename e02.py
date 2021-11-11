# 2. Дополнить следующую функцию недостающим кодом:
import os
from pprint import pprint


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    # заполните далее
    dirs, files = [], []
    inner = []
    for path in os.listdir(sPath):
        full_path = os.path.join(sPath, path)
        if os.path.isdir(full_path):
            dirs.append(path)
            inner += print_directory_contents(full_path)
        else:
            files.append(path)
    return [(sPath, dirs, files)] + inner


pprint([p for p in print_directory_contents(os.curdir)][:5])

# [('.', ['.idea', 'venv'], ['e01.py', 'e02.py']),
#  ('.\\.idea',
#   ['inspectionProfiles'],
#   ['.gitignore',
#    'gb_prepare_hr.iml',
#    'misc.xml',
#    'modules.xml',
#    'workspace.xml']),
#  ('.\\.idea\\inspectionProfiles', [], ['profiles_settings.xml']),
#  ('.\\venv', ['Lib', 'Scripts'], ['.gitignore', 'pyvenv.cfg']),
#  ('.\\venv\\Lib', ['site-packages'], [])]
