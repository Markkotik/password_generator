"""Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку
на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

Составляющие проекта:

Целые числа (тип int);
Переменные;
Ввод / вывод данных (функции input() и print());
Условный оператор (if/elif/else);
Цикл for;
Написание пользовательских функций;
Работа с модулем random для генерации случайных чисел."""

from random import choice

# создаю переменные всех видов символов, которые могут быть задействованы в генерации пароля,
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

# Считывание пользовательских данных:

print('Здравствуйте, это генератор безопасных паролей, пожалуйста, ответьте на вопросы:')

password_quantity = int(input('Количество паролей для генерации'))
password_len = int(input('Длину одного пароля'))
password_digits = input('Включать ли цифры? (д = да, н = нет) ').strip()
password_uppercase = input('Включать ли прописные буквы (д = да, н = нет) ?').strip()
password_lowercase = input('Включать ли строчные буквы (д = да, н = нет) ?').strip()
password_punctuation = input(f'Включать ли символы {punctuation} (д = да, н = нет) ?').strip()
password_exceptions = input('Исключать ли неоднозначные символы il1Lo0O (д = да, н = нет) ?').strip()

# Настройка генерируемых паролей:

if password_digits.lower() == 'д':  # Все символы выбранные пользователем мы добавляем в одну строку
    chars += digits
if password_uppercase.lower() == 'д':
    chars += uppercase_letters
if password_lowercase.lower() == 'д':
    chars += lowercase_letters
if password_punctuation.lower() == 'д':
    chars += punctuation
if password_exceptions.lower() == 'д':  # Удаляем символы, которые можно спутать с другими
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


# Функция генерации пароля:

def generate_password(password_len, chars):
    password = ''
    for j in range(password_len):
        password += choice(chars)
    return password


# Генерация нужного количества паролей:

for i in range(password_quantity):
    print('Ваш надежный пароль: ', generate_password(password_len, chars))
