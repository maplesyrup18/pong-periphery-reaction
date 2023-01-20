import sys
import random
from game import pong, leaderboard

player=input('Nickname please: ')
print("Welcome to the tester, do you consent with us recording your results? Your nickname will be anonymized\n")
consent_input=input('Yes (Y) / No (N): ')
consent = False
if(consent_input == "yes" or "Y" or "y" or "Yes"):
    consent = True
else: 
    consent = False
print('Your response has been recorded.\nModule 1 of the tester has started.')

player_identifier = random.randrange(1, 50000)

#play module 1
first_game = pong.pong(0, player_identifier, consent)
print("You scored: "+str(first_game))

#play module 2
input("Input anything to continue to the next level: ")
second_game = pong.pong(1, player_identifier, consent)
print("You scored: "+str(second_game))

#play module 3
input("Input anything to continue to the next level: ")
final_game = pong.pong(2, player_identifier, consent)
print("You scored: "+str(final_game))

final_score = first_game+second_game+final_game
print("Your final score is: "+str(final_score))
save_response = input("Do you wish to save your score on the leaderboard?: Y/N: ")

if(save_response == "yes" or "Y" or "y" or "Yes"):
    leaderboard.save_final_scores(final_score, player)
    print("Thanks a lot! We'll let you know if you get the chocolate")

else: 
    print("Thanks for your participation")