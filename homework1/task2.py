# Задание 2. (повышенной сложности)
#
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, в
# котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation
# модуля string). В этом режиме должно проверяться наличие слова в выводе.


import subprocess
import string

def check_command_output(cmd, word):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    # print(out)
    translator = str.maketrans("", "", string.punctuation)
    output_words = out.translate(translator).split()
    # print(output_words)
    if result.returncode == 0:
        if word in output_words:
            return True
        else:
            return False


if __name__ == '__main__':
    command = "cat /etc/os-release"
    word_to_find = "Jammy"
    res = check_command_output(command, word_to_find)

    if res:
        print(f"Команда выполнена успешно и слово '{word_to_find}' найдено в выводе.")
    else:
        print(f"Команда не выполнена успешно или слово '{word_to_find}' не найдено в выводе.")

