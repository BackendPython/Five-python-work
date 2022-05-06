import random

city = ['Toshkent','Andijon','Nukus']

t = 1
while t==1:
    turn = random.choice(city)
    print(f"Tasodifiy shahar tanlandi: {turn}")
    t = 0
    quest = input('Tasodifiy tanlashga ruxsat berasizmi? (uz/eng): ').lower()
    if quest=='ha':
        t = 1
    elif quest=='yes':
        t = 1
    else:
        print('Bo`ldi... Shaxarga bilet tugadi🤣')