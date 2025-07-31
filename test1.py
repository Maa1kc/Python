kids = ['Витя', 'Маша', 'Марина']
candies = ['Батончик', 'Сникерс', 'Мишка Косолапый', 'Коровка']

for kid in kids:
    for candy in candies:
        print(kid, 'получает конфету', candy)

bunny_counter = ''  # Создали переменную bunny_counter, её значение - пустая строка.

for i in range(1, 6):
    # На каждой итерации цикла
    # к переменной bunny_counter будет дописываться
    # очередная цифра, запятая и пробел (чтобы числа в строке не слиплись).
    # Получившееся значение будет присвоено той же переменной bunny_counter
    bunny_counter = bunny_counter + str(i) + ', '

print(bunny_counter + 'вышел зайчик погулять!')

total_sum = sum(range(1, 101))
print(total_sum)
print(True)
# Без неожиданностей, будет напечатано: True

print(not True)
# Будет напечатано: False

print(not False)
# Будет напечатано: True


x = 44

if x < 45 and x != 42 or not x > 40:
    print("Выражение вернуло True!")
else:
    print("Выражение вернуло False!")

# Объявление функции hello()
def hello():
    # А здесь началось тело функции
    print('Приветствую тебя, джедай Питона!')

hello()
hello()
hello()

# Объявление функции с параметром name
def hello(name):
    # Параметр name можно обрабатывать в теле функции:
    print(name + ', приветствую тебя!')

# Вызов функции с аргументом 'Максим'
hello('Максим')
# Будет напечатано: Максим, приветствую тебя!

# Раскомментируйте строку ниже, в качестве аргумента подставьте своё имя -
# и снова выполните код.
hello('Михаил')

# Теперь у функции hello() два параметра: name и bonus
def hello(name, bonus):
    # Оба параметра применим в теле функции:
    print(name + ', приветствую тебя! Бери ' + bonus)


hello('Дарт Вейдер', 'печеньки')

# И ещё раз вызовем, с другими аргументами:
hello('Винни Пух', 'мёд')

# Раскомментируйте вызов функции, подставьте в него аргументы
# и вновь запустите код
hello('Михаил', 'что-то вкусное')

# Код функции say_hello()
def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
    elif current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')

# Дальше код написан без отступов: этот код уже вне функции.

# Несколько раз вызовем функцию say_hello() с разными аргументами:
say_hello(4)  # Вызов функции say_hello() с аргументом 4
say_hello(10)  # Вызов функции с аргументом 10
say_hello(15)  # Ещё один вызов функции
say_hello(20)  # И ещё один вызов

#Функция по расчету числ Фибоначчи:
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=', ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(200000)


# функция для вычисления
# периметра прямоугольника
# от англ. calculate, ”вычислять”
def calc_perimeter(side_a, side_b):
    return (side_a + side_b) * 2
# функция для вычисления
# площади прямоугольника
def calc_square(side_a, side_b):
    return side_a * side_b
# здесь подготовка результата
def show_info(side_a, side_b):
    p = calc_perimeter(side_a, side_b)
    s = calc_square(side_a, side_b)
    text = 'Периметр = ' + str(p) + ' м., '
    text += 'площадь = ' + str(s) + ' кв.м.'
    return text
a = 8
b = 10
print(show_info(a, b))
# можем произвести расчёты
# и для другого прямоугольника
print(show_info(3, 4))

def print_friends_count(friends_count):
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)


# Ниже напишите цикл, в котором будет вызываться функция print_friends_count
# с аргументом от 0 до 20 включительно
for friends_count in range(21):
    print_friends_count(friends_count)

# Количество баллов, которое студент получил за тест.
score = 60

def test_score():
    if score > 50:
        print('Отличная работа!')
        print('Тест сдан.')
    else:
        print('Хорошая попытка!')
        print('Вы отлично постарались, но нужно подготовиться чуть получше.')
        print('Ещё раз пройти тестирование можно в следующую среду.')

test_score()

# Добавим значение по умолчанию для аргумента name
def print_home(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

# Передаём именованный параметр:
# явно указываем, что значение 'Земля' предназначено для параметра planet
print_home(planet='Земля')

# Ещё раз вызовем функцию: передадим два именованных параметра,
# но не в том порядке, как они указаны в объявлении функции:
print_home(planet='Марс', name='Макс Калдырь')

#######################
#Список со всеми площадями комнат в помещении:
flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

# Сохраним искомое значение в переменной, так будет проще работать.
room_size = 22.19

# В переменной count будем подсчитывать
# количество обнаруженных помещений нужной площади.
# Пока что она равна нулю.
count = 0

# Объявляем цикл: из списка flat все значения по очереди будут передаваться
# в переменную room
for room in flat:
    # Проверяем, равно ли значение переменной room искомому значению
    if room == room_size:
        # Если значения room и room_size равны -
        # переменной count присваиваем её предыдущее значение,
        # увеличенное на единицу
        count += 1 # тоже самое, что count = count + 1

# Этот код выполнится только после того,
# как цикл переберёт все элементы списка flat.
# В переменной count будет сохранено количество помещений с площадью 22.19
print('Комнат площадью', room_size, 'кв.м:', count)

flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

# В переменной sum_area будем суммировать площади комнат.
# Пока что она равна нулю.
sum_area = 0

for room in flat:
    # На каждой итерации цикла прибавляем к sum_area площадь ещё одной комнаты
    # Запишем эту операцию через сокращённый синтаксис +=
    sum_area += room

print('Общая площадь =', sum_area)

# Список годов, в которые Depeche Mode выпускала альбомы
years = [
    1981, 1982, 1983, 1984, 1986, 1987, 1990,
    1993, 1997, 2001, 2005, 2009, 2013, 2017
]

# В этой переменной будем подсчитывать количество альбомов.
# Пока что в ней ничего нет, она равна нулю.
count = 0

for year in years:
    if year > 2000:
        # Каждый раз загибаем по одному пальцу,
        # обнаружив альбом, выпущенный в 21 веке.
        count += 1   # Это то же самое, что count = count + 1

print('Выпущено альбомов в XXI веке:', count)

# Объявите функцию rooms_equal() с параметрами room_size и room_list
def rooms_equal(room_size, room_list):
# Перенесите следующий код в тело функции, которую вы объявили
    count = 0

    for room in room_list:
        if room == room_size:
            count += 1

    print('Комнат площадью', room_size, 'кв.м:', count)


# Следующий код не изменяйте и не переносите в тело функции
flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]

rooms_equal(5.55, flat)
# Добавьте ещё один вызов функции rooms_equal()
# Передайте в функцию искомую площадь - 9.2 кв.м и список hut
rooms_equal(9.2, hut)

may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]

def comfort_count(temperatures):
    # Напишите код функции
    count = 0
    for temp in temperatures:
        if temp >= 22 and temp <= 26: #тоже самое: if 22 <= temp <= 26:
            count +=1
    print('Количество тёплых дней в этом месяце:', count)

# Дальше код не меняйте
comfort_count(may_2017)  # Узнаем, что было в мае 2017 г.
comfort_count(may_2018)  # Узнаем, что было в мае 2018 г.


#Словари итоговые задачи
#1
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

#2

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        # Чтобы получить перечень друзей -
        # переберите словарь DATABASE в цикле
        for name in DATABASE:
             friends_string += (name + ' ')     # Добавляйте к переменной friends_string имя друга и пробел
        # Верните строку, составленную из 'Твои друзья: ' и friends_string
        return('Твои друзья: ' + friends_string)
    elif query == 'Где все мои друзья?':
        return 'Я поняла, это вопрос про города!'
    else:
        return '<неизвестный запрос>'

# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

#3

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        # Чтобы получить перечень друзей -
        # переберите словарь DATABASE в цикле
        for name in DATABASE:
            friends_string += (name + ' ')  # Добавляйте к переменной friends_string имя друга и пробел
        # Верните строку, составленную из 'Твои друзья: ' и friends_string
        return ('Твои друзья: ' + friends_string)
    elif query == 'Где все мои друзья?':
        cities_string = ''
        for city in set(DATABASE.values()):
            cities_string += city + ' '

        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'


# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))


monument_string = 'Я памятник себе воздвиг нерукотворный'

index_list = [0, 1, 2, 8, 6, 17, 24]

for i in index_list:
    # На каждой итерации цикла
    # берём из строки monument_string элемент с индексом i и печатаем полученную букву
    print(monument_string[i])

# Обратимся к элементам списка по отрицательным индексам
friends = ['Сергей', 'Соня', 'Миша', 'Дима', 'Алина']
print(friends[-3])  # Миша
print(friends[-5])  # Сергей

# То же и со строкой
monument_string = 'Я памятник себе воздвиг нерукотворный'
print(monument_string[-2])   # ы
print(monument_string[-37])  # Я

milk_str = 'молоковоз'

# Применяем метод split() с аргументом 'о':
new_list = milk_str.split('о')

print(new_list)
# Будет напечатано: ['м', 'л', 'к', 'в', 'з']

message = 'У меня опять всё сломалось и не работает соединение с интернетом!!11'

# Разбиваем сообщение по пробелам на слова
words = message.split()
# Проверяем, есть ли ключевые слова в письме
if 'стоимость' in words:
    print('Переслать письмо в отдел биллинга')
elif 'сломалось' in words:
    print('Переслать письмо в техподдержку')
else:
    print('Содержание письма не определено, придётся прочесть самостоятельно')

quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    word_list = message.split()
    return word_list[-3]

# Вызовы функции готовы к работе, не изменяйте их!

# Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
print(penult_word(quote_1))

# То же, но с аргументом quote_2.
print(penult_word(quote_2))

# То же с аргументом quote_3.
print(penult_word(quote_3))

def check_query(query):
# Допишите код тела функции
    elements  = query.split(', ')
    if 'Анфиса' in elements:
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'



# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

# Напечатаем результат.
# Переберём список вопросов в цикле
for q in queries:
    # Каждый из вопросов передадим аргументом
    # в функцию check_query()
    result = check_query(q)
    # И для каждого вызова напечатаем вопрос и, через дефис - вердикт программы
    print(q, '-', result)

def check_query(query):
    elements  = query.split(', ')
    # Напишите код функции
    return elements[-1]

# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '—', result)

    DATABASE = {
        'Серёга': 'Омск',
        'Соня': 'Москва',
        'Миша': 'Москва',
        'Дима': 'Челябинск',
        'Алина': 'Красноярск',
        'Егор': 'Пермь',
        'Коля': 'Красноярск'
    }


    def process_anfisa(query):
        if query == 'Сколько у меня друзей?':
            count = len(DATABASE)

            return 'У тебя ' + str(count) + ' друзей.'
        elif query == 'Кто все мои друзья?':
            # Из словаря DATABASE создайте строку с помощью join();
            # имена друзей разделите запятой и пробелом.
            # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
            friends_string = ', '.join(list(DATABASE))

            # Этот цикл больше не понадобится, удалите его

            return 'Твои друзья: ' + friends_string
        elif query == 'Где все мои друзья?':
            unique_cities = set(DATABASE.values())
            # Из сета unique_cities создайте строку с помощью join();
            # названия городов разделите запятой и пробелом.
            # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
            cities_string = ', '.join(unique_cities)

            # Этот цикл больше не понадобится, удалите его

            return 'Твои друзья в городах: ' + cities_string
        else:
            return '<неизвестный запрос>'


    print('Привет, я Анфиса!')
    print(process_anfisa('Сколько у меня друзей?'))
    print(process_anfisa('Кто все мои друзья?'))
    print(process_anfisa('Где все мои друзья?'))


# Выражения в f-строках
# 1
def print_time(hour, minute, second):
    print(f'На часах {hour}:{minute}:{second}')  # Аргумент должен содержать f-строку

print_time('19', '28', '06')

# 2
def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    lenght_song = len(listened)
    return f'Вы прослушали {lenght_song} песен.'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

# 3
def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    lenght_song = len(listened)
    summ = 0
    for sec in listened:
        summ += sec
    total_summ = summ//60
        #rint(int(summ/60))
    #time_song = sum(listened)
    return f'Вы прослушали {lenght_song} песен общей продолжительностью {total_summ} минут.'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

#3.2 Неправильное решение с правильным результатом

def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    total_duration = 0
    for duration in listened:
        total_duration += duration
    total_duration = int(total_duration/60)
    return f"Вы прослушали {len(listened)} песен общей продолжительностью {total_duration} минут."

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

# 4

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        # В следующей строке замените конкатенацию на f-строку
        return f'У тебя {count} друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        # В следующей строке замените конкатенацию на f-строку
        return f'Твои друзья: {friends_string}'
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        # В следующей строке замените конкатенацию на f-строку
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

# Запросы к друзьям
# 1

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья"
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга.'
    else:
        return f'{friends_count} друзей.'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение,
        # которое вернёт функция format_friends_count()
        return f'У тебя {format_friends_count(count)}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('сколько у меня друзей?'))
print(process_anfisa('кто все мои друзья?'))
print(process_anfisa('где все мои друзья?'))
print(process_anfisa('кто виноват?'))

# 2

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья"
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_query(query):
        query_list = query.split(', ')
        if query_list[0] == 'Анфиса':
            return process_anfisa(query_list[1])
        else:
            return

def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение,
        # которое вернёт функция format_friends_count()
        #last_count = format_friends_count(count)
        return f'У тебя {format_friends_count(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'




print('Привет, я Анфиса!')
print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))

# 3

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья"
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга.'
    else:
        return f'{friends_count} друзей.'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение,
        # которое вернёт функция format_friends_count()
        return f'У тебя {format_friends_count(count)}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_query(query):
    query_list = query.split(', ')
    name = query_list[0]
    if name == 'Анфиса':
        return process_anfisa(query)
    else:
        return process_friend(name, query)


def process_friend(name, query):
    if name in DATABASE:
        if 'ты где?' in query:
            return f'{name} в городе {DATABASE[name]}'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


print('Привет, я Анфиса!')
print(process_anfisa('сколько у меня друзей?'))
print(process_anfisa('кто все мои друзья?'))
print(process_anfisa('где все мои друзья?'))
print(process_anfisa('кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))

from random import randint

print(
    "Вывод случайного целого числа ",
    randint(0, 9),
)  # например, 5
print(
    "Вывод случайного целого числа ",
    randint(0, 9),
)  # например, 0

# Импорт библиотеки math.
import math

# Теперь в программе можно применять любые функции из неё.
square_root = math.sqrt(16)
print(square_root)

from random import choice  # Импорт одной функции из библиотеки

def find_a_present(prizes):
    # Обращаемся к функции напрямую: choice(), а не random.choice()
    return choice(prizes)

print(find_a_present(['кукла', 'жвачка', 'игрушечный питон']))
print(find_a_present(['мяч', 'чебурашка', 'лосяш']))

