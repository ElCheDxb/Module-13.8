ticket = int(input('Сколько билетов Вы хотите приобрести: '))
summa = 0

age = int(input('Сколько лет участнику? '))
if age >= 25:
    cost = 1390
elif 25 > age >= 18:
    cost = 990
elif age < 18:
    cost = 0

summa = summa + cost

for N in range(1, ticket):
    age = int(input('Сколько лет следующему  участнику? '))
    if age >= 25:
        cost = 1390
    elif 25 > age >= 18:
        cost = 990
    elif age < 18:
        cost = 0
    summa = summa + cost

if ticket <= 3:
        print('Сумма к оплате', summa, 'рублей')
else:
    summa = 0.9 * summa
    print('Сумма к оплате с учетом скидки', summa, 'рублей')
