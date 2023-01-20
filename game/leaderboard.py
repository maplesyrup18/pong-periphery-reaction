import pandas as pd
import random
path = 'C:\\Users\\aceas\\Desktop\\School\\Human in the Loop\\Project'

def save_scores_txt(reaction_times, positions, speed, number):
    reaction_df = pd.DataFrame()
    reaction_df['reaction_times']=reaction_times
    reaction_df["positions"] = positions

    reaction_df.to_csv(path+'\\analysis\\data\\difficulty'+str(speed)+'\\subject'+str(number))

def save_final_scores(final_score, nickname):
    score_df = pd.read_csv(path+'\\analysis\\data\\leaderboard.csv')
    temp_score_df=pd.DataFrame([nickname, final_score], columns=["name", "score"], index=[1])
    score_df.append(temp_score_df, ignore_index=True)
    sorted_score = score_df.sort_values(by='score')
    print(sorted_score)

    sorted_score.to_csv(path+'\\analysis\\data\\leaderboard.csv', mode='w+')
    
