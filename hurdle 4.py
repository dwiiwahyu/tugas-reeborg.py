def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def wall_front():
    while wall_on_right():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
     
while not at_goal():
    if wall_in_front():
        turn_left()
        wall_front()
        turn_left()
    else:
        move()
