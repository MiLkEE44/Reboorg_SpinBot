# Will make Reeborg's World robot spin around,
# hugging and moving along walls
# or going straight if there is no wall.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def hop():
    if wall_in_front() == True:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    else:
        move()

def big_wall():
    if wall_in_front() == True:
        turn_left()
    else:
        move()

def down():
    while wall_in_front() == False:
        if at_goal() == True:
            done()
        else:
            move()
            turn_right()

def walk():
    while front_is_clear():
        move()

number_of_hurdles = 100
for hurdles in range(number_of_hurdles):
    if at_goal() == True:
        done()
    elif not at_goal():
        walk()
        big_wall()
        down()
