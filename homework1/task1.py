# Задание 1. Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в ее выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.

import subprocess


def check_text_in_command(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        if text in result.stdout:
            return True
        else:
            return False


if __name__ == '__main__':
    command = "ls"
    text_to_find = "task1.py"
    result = check_text_in_command(command, text_to_find)

    if result:
        print(f"Команда выполнена успешно и текст '{text_to_find}' найден в выводе.")
    else:
        print(f"Команда не выполнена успешно или текст '{text_to_find}' не найден в выводе.")
