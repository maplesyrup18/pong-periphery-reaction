from game import generate_schedule, playpong

def pong(difficulty, player_identifier, consent):
    time = 2
    schedule = generate_schedule.generate_schedule(time, 12)
    game= playpong.playpong(schedule,1000,time)
    match difficulty:
        #center, no game
        case 0:
            game = playpong.playpong(schedule, 10, time)
        #center, game easy
        case 1:
            game=playpong.playpong(schedule, 15, time)
        #center, game fast
        case 2:
            game=playpong.playpong(schedule, 20, time)

    score = game.play(player_identifier, consent)
    return score
