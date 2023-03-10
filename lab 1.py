b = input('Masz dzis urodziny. Tak lub Nie: ')
speed = int(input('Podaj prędkość Pojazdu: '))
if b == 'Tak':
    speed -= 5

    if speed >= 61 and speed <= 80:
        print('Mały Mandat')
    elif speed > 81:
        print('Duży Mandat')
    else:
        print('Brak Mandatu')

else:
    if speed >= 61 and speed <= 80:
        print('Mały Mandat')
    elif speed >= 81:
        print('Duży Mandat')
    else:
        print('Brak Mandatu')
