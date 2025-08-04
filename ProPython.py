def practicum():
    args = {
        0: 'Практикум',
        1: 'Яндекс',
    }
    args[0] = 'Яндекс'
    args[1] = 'Практикум'
    return [a for a in args.keys()]

print(practicum())

day_1 = 1.434
day_2 = 2.12
day_3 = 1.632
day_4 = 5.59
day_5 = 2.542
day_6 = 1.1
day_7 = 1.324

week_dist = day_1*1000 + day_2*1000 + day_3*1000 + day_4*1000 + day_5*1000 + day_6*1000 + day_7*1000

print(week_dist/1000)

# Получаем данные в секундах
res = 424562
# Переведите полученное значение в необходимые единицы измерения
days = res // (24*3600)
hours = (res // 3600) % 24
minutes = (res // 60) % 60
seconds = res % (days*24*3600 + hours*3600 + minutes*60)

print(days, hours, minutes, seconds)