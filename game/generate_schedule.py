'''Time in minutes, generates a schedule of appearences of the buttons with a minimum of 5 seconds difference
Always unique number... Might have high complexity whoops'''
import random


def generate_schedule(time, amount_of_buttons):

    s_time=time*60
    schedule = []

    #division by 6 just to make sure... 1 second to press...
    if(s_time / 6) < amount_of_buttons:
        print("Too short time for this amount of buttons")


    while len(schedule) < amount_of_buttons:
        new_time = random.randint(2, s_time-5)
        if all(abs(new_time - time) >= 5 for time in schedule):
            schedule.append(new_time)                
    schedule.sort()
    return schedule


                

