# Добавить в проект тесты, проверяющие работу команд  d (удаление из архива) и u (обновление архива).
# Вынести  в отдельные переменные пути к папкам с файлами, с архивом  и с распакованными файлами.
# Выполнить тесты с ключом -v.

import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def getout(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout

