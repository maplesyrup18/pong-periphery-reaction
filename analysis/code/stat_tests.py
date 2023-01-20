import pandas as pd
from scipy import stats

#this is bad code
path = 'C:\\Users\\aceas\\Desktop\\School\\Human in the Loop\\Project\\analysis\\data\\difficulty'
subject1 = pd.read_csv(path+'10\\subject1471')
subject2 = pd.read_csv(path+'10\\subject8224')
subject3 = pd.read_csv(path+'10\\subject9897')
subject4 = pd.read_csv(path+'10\\subject32041')
subject5 = pd.read_csv(path+'10\\subject35982')
subject6 = pd.read_csv(path+'10\\subject43634')

subject1_diff2 = pd.read_csv(path+'15\\subject1471')
subject2_diff2 = pd.read_csv(path+'15\\subject8224')
subject3_diff2 = pd.read_csv(path+'15\\subject9897')
subject4_diff2 = pd.read_csv(path+'15\\subject32041')
subject5_diff2 = pd.read_csv(path+'15\\subject35982')
subject6_diff2 = pd.read_csv(path+'15\\subject43634')

subject1_diff3 = pd.read_csv(path+'20\\subject1471')
subject2_diff3 = pd.read_csv(path+'20\\subject8224')
subject3_diff3 = pd.read_csv(path+'20\\subject9897')
subject4_diff3 = pd.read_csv(path+'20\\subject32041')
subject5_diff3 = pd.read_csv(path+'20\\subject35982')
subject6_diff3 = pd.read_csv(path+'20\\subject43634')

all_subjects_diff1 = pd.DataFrame(subject1)
all_subjects_diff1.append(subject2, ignore_index=True)
all_subjects_diff1.append(subject3, ignore_index=True)
all_subjects_diff1.append(subject4, ignore_index=True)
all_subjects_diff1.append(subject5, ignore_index=True)
all_subjects_diff1.append(subject6, ignore_index=True)

all_subjects_diff2 = pd.DataFrame(subject1_diff2)
all_subjects_diff2.append(subject2_diff2, ignore_index=True)
all_subjects_diff2.append(subject3_diff2, ignore_index=True)
all_subjects_diff2.append(subject4_diff2, ignore_index=True)
all_subjects_diff2.append(subject5_diff2, ignore_index=True)
all_subjects_diff2.append(subject6_diff2, ignore_index=True)

all_subjects_diff3 = pd.DataFrame(subject1_diff3)
all_subjects_diff3.append(subject2_diff3, ignore_index=True)
all_subjects_diff3.append(subject3_diff3, ignore_index=True)
all_subjects_diff3.append(subject4_diff3, ignore_index=True)
all_subjects_diff3.append(subject5_diff3, ignore_index=True)
all_subjects_diff3.append(subject6_diff3, ignore_index=True)

#
all_left_diff1 = all_subjects_diff1.loc[all_subjects_diff1['positions']=='left']
all_leftwiggle_diff1 = all_subjects_diff1.loc[all_subjects_diff1['positions']=='left+wiggle']
all_centre_diff1 = all_subjects_diff1.loc[all_subjects_diff1['positions']=='center-of-game']
#ttest for wiggle, centre and left
print(stats.wilcoxon(all_left_diff1['reaction_times'], all_centre_diff1['reaction_times']))
print(stats.ttest_ind(all_left_diff1['reaction_times'], all_leftwiggle_diff1['reaction_times']))

#
all_left_diff2 = all_subjects_diff2.loc[all_subjects_diff2['positions']=='left']
all_leftwiggle_diff2 = all_subjects_diff2.loc[all_subjects_diff2['positions']=='left+wiggle']
all_centre_diff2 = all_subjects_diff2.loc[all_subjects_diff2['positions']=='center-of-game']
#ttest for wiggle, centre and left 
print(stats.ttest_ind(all_left_diff2['reaction_times'], all_centre_diff2['reaction_times']))
print(stats.ttest_ind(all_left_diff2['reaction_times'], all_leftwiggle_diff2['reaction_times']))


#
all_left_diff3 = all_subjects_diff3.loc[all_subjects_diff3['positions']=='left']
all_leftwiggle_diff3 = all_subjects_diff3.loc[all_subjects_diff3['positions']=='left+wiggle']
all_centre_diff3 = all_subjects_diff2.loc[all_subjects_diff3['positions']=='center-of-game']
#ttest for wiggle and left
print(stats.ttest_ind(all_left_diff3['reaction_times'], all_centre_diff3['reaction_times']))
print(stats.ttest_ind(all_left_diff3['reaction_times'], all_leftwiggle_diff3['reaction_times']))


#ttest between left on low and high difficulty
print(stats.ttest_ind(all_left_diff1['reaction_times'], all_left_diff3['reaction_times']))
