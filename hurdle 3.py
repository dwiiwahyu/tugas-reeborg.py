def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def pass_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        pass_wall()
    else:
        move()
