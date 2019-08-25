# https://www.codingame.com/training/easy/power-of-thor-episode-1

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
x = initial_tx
y = initial_ty

while True:
    remaining_turns = int(input())

    if x < light_x and y < light_y:
        i = 'SE'
        x += 1
        y += 1
    elif x > light_x and y < light_y:
        i = 'SW'
        x -= 1 
        y += 1
    elif x > light_x and y > light_y:
        i = 'NW'
        x -= 1
        y -= 1
    elif x < light_x and y > light_y:
        i = 'NE'
        x += 1
        y -= 1
    elif x > light_x:
        i = 'W'
        x -= 1
    elif x < light_x:
        i = 'E'
        x += 1
    elif y > light_y:
        i = 'N'
        y -= 1
    elif y < light_y:
        i = 'S'
        y += 1
    
    print(i)
