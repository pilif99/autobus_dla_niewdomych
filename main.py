import math

x = int(input('Proszę podać zarezerwowane miejsce: '))
if x == 1:
    print('biedny konduktor')
else:
    row = math.ceil((x-1)/5)
    if math.fmod((x-1), 5) == 0:
        column = 'W'
        if math.fmod((row), 2) == 0:
            LorR = 'L'
        else:
            LorR = 'R'
    elif math.fmod((x-1), 5) == 1:
        column = 'W'
        if math.fmod((row), 2) == 0:
            LorR = 'R'
        else:
            LorR = 'L'
    elif math.fmod((x-1), 5) == 2:
        if math.fmod((row), 2) == 0:
            LorR = 'R'
            column = 'M'
        else:
            LorR = 'L' 
            column = 'A'
    elif math.fmod((x-1), 5) == 3:
        LorR = 'R'
        column = 'A'
    elif math.fmod((x-1), 5) == 4:
        if math.fmod((row), 2) == 0:
            LorR = 'L'
            column = 'A'
        else:
            LorR = 'R' 
            column = 'M'

print(f'{row} {column} {LorR}')
