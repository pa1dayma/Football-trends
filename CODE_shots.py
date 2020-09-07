# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:06:27 2020

@author: Pawan Dayma

This code takes in the statsbomb data sets provided by them publicly.
I've done analysis for La Liga season 2018/2019 and La Liga 2006/2007. 

"""

import matplotlib.pyplot as plt


#Reading file La Liga 2018/2019
competition_id=11
season_id=4
file_name='DIRECTORY/Statsbomb/data/matches/'+str(competition_id)+'/'+str(season_id)+'.json'

import json
with open(file_name,'r',encoding='utf-8') as m:
    matches = json.load(m)

#Size of the pitch in yards (!!!)
pitchLengthX=120
pitchWidthY=80
#VAriable count for shots inside or outside of box
inside_box=0
outside_box=0
#Draw the pitch
#The code for plotting pitch can found on FCPython's website
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

for match in matches:
    file_name=str(match['match_id'])+'.json'
    #Load in all match events 
    import json
    with open('DIRECTORY/Statsbomb/data/events/'+file_name,'r',encoding='utf-8') as data_file:    
         data = json.load(data_file)
         
    #get the nested structure into a dataframe 
    #store the dataframe in a dictionary with the match id as key (remove '.json' from string)
    from pandas.io.json import json_normalize
    df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
    
    #Extracting shots
    shots=df.loc[df['type_name']=='Shot'].set_index('id')

    #Plotting shots
    for i,shot in shots.iterrows():
        x=shot['location'][0]
        y=shot['location'][1]
        if x>102 and y>22 and y<58:
            inside_box=inside_box+1
        else:
            outside_box=outside_box+1
            
        goal=shot['shot_outcome_name']=='Goal'
        team_name=shot['team_name']
    
        circleSize=0.7
        
        if goal:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="green")
             
        else:            
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")     
            shotCircle.set_alpha(.2)
        ax.add_patch(shotCircle)
#Calculating average shots per match
avg_shots=round((inside_box+outside_box)/len(matches),2)
avg_inside=round(inside_box/len(matches),2)
avg_outside=round(outside_box/len(matches),2)  

        
plt.text(3, 75,'La Liga season 2018/2019',fontsize=8)                
plt.text(3,71,'Avg.shots per game='+str(avg_shots),fontsize=8)
plt.text(3,67,'Avg. shots taken from inside the box='+str(avg_inside),fontsize=8)
plt.text(3,63,'Avg. shots taken from outside the box='+str(avg_outside),fontsize=8) 
fig.set_size_inches(10, 7)
fig.savefig('DIRECTORY/Statsbomb/output/la_liga_18_19.pdf', dpi=100)               
        

#BELOW IS BASICALLY THE SAME CODE FOR DIFFERENT SEASON
        
#Reading file La Liga 2006/2007
competition_id=11
season_id=39
file_name='DIRECTORY/Statsbomb/data/matches/'+str(competition_id)+'/'+str(season_id)+'.json'

import json
with open(file_name,'r',encoding='utf-8') as m:
    matches = json.load(m)

#Size of the pitch in yards (!!!)
pitchLengthX=120
pitchWidthY=80
#VAriable count for shots inside or outside of box
inside_box=0
outside_box=0
#Draw the pitch
from FCPython import createPitch
(fig,bx) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

for match in matches:
    file_name=str(match['match_id'])+'.json'
    #Load in all match events 
    import json
    with open('DIRECTORY/Statsbomb/data/events/'+file_name,'r',encoding='utf-8') as data_file:    
         data = json.load(data_file)
         
    #get the nested structure into a dataframe 
    #store the dataframe in a dictionary with the match id as key (remove '.json' from string)
    from pandas.io.json import json_normalize
    df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
    
    #Extracting shots
    shots=df.loc[df['type_name']=='Shot'].set_index('id')

    #Plotting shots
    for i,shot in shots.iterrows():
        x=shot['location'][0]
        y=shot['location'][1]
        if x>102 and y>22 and y<58:
            inside_box=inside_box+1
        else:
            outside_box=outside_box+1
            
        goal=shot['shot_outcome_name']=='Goal'
        team_name=shot['team_name']
    
        circleSize=0.7
        
        if goal:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="green")
             
        else:            
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")     
            shotCircle.set_alpha(.2)
        bx.add_patch(shotCircle)

#Calculating average shots per match
avg_shots=round((inside_box+outside_box)/len(matches),2)
avg_inside=round(inside_box/len(matches),2)
avg_outside=round(outside_box/len(matches),2)  

        
plt.text(3, 75,'La Liga season 2006/2007',fontsize=8)                
plt.text(3,71,'Avg.shots per game='+str(avg_shots),fontsize=8)
plt.text(3,67,'Avg. shots taken from inside the box='+str(avg_inside),fontsize=8)
plt.text(3,63,'Avg. shots taken from outside the box='+str(avg_outside),fontsize=8) 
fig.set_size_inches(10, 7)
fig.savefig('DIRECTORY/Statsbomb/output/la_liga_06_07.pdf', dpi=100)       


#END OF CODE