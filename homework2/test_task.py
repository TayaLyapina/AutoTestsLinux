 Задание 1.
# Условие:
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
#
# *Задание 2. *
#
# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.

from task import checkout, getout
import subprocess


folder_in = '/home/taya/folder_in/'
folder_out = '/home/taya/folder_out/'
folder_ext = '/home/taya/folder_ext/'


def test_step1():
    assert checkout(f"cd {folder_out}; 7z l arh.7z", "Listing archive: arh.7z"), "test1 FAIL"


def test_step2():
    assert checkout(f"cd {folder_ext}; 7z x {folder_out} -y", "Everything is Ok"), "test2 FAIL"


def test_step3():
    res = checkout(f"cd {folder_in}; 7 h file1.txt", "Everything is Ok")
    crc32_h = getout(f"cd {folder_in}; crc32 test1.txt").upper()
    res2 = checkout(f"cd {folder_in}; 7z h file1.txt", crc32_h)
    assert res and res2, "test3 FAIL"