"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове."""

user_str = input('введите слова через пробел\n>>> ')
for ind, el in enumerate(user_str.split(), 1):
    print(ind, el[:10])
