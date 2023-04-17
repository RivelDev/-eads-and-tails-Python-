import random, time

infinity = 'Да'
while infinity == 'Да':
    results = ['Выпал орел', 'Выпала решка']
    start = input('Игрок 1: Орел или Решка?: ')
    start2 = input('Игрок 2: Орел или Решка?: ')
    print(f'Игрок 1 выбрал {start}, игрок 2 выбрал {start2}')
    if start == start2:
        print('Выбирите другую сторону!')
        quit()
    if start == 'Орел' and start2 != 'Орлу':
        print('Игрок 1 выбрал орла...')
        print('Игрок 2 выбрал решку...')
        time.sleep(3)
        print('*Подброшена монета...*')
        time.sleep(1)
        result = random.choice(results)
        print(result)
    elif start == 'Решка' and start2 != 'Решка':
        print('Игрок 1 выбрал решку...')
        print('Игрок 2 выбрал орла...')
        time.sleep(3)
        print('*подброшена монета...*')
        time.sleep(1)
        result = random.choice(results)
        print(result)
    else:
        print('Error...')
        time.sleep(0.5)
        quit()
infinity = input('Играем дальше? [Да|Нет]: ')