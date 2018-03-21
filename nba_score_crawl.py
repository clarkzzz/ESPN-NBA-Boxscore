#%%
# environment setup
from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np

#%%
# obtain url and convert to BS format
url = 'http://www.espn.com/nba/boxscore?gameId=400975805'
response = requests.get(url)
content = response.content
parser = BeautifulSoup(content, 'html.parser')

#%%
# grab boxscore table data from html table
boxscore = parser.select('tr')

#%%
# drop non-player data in the table
# if the number of attributes in a player row is 15 (participated in the game, thus having 15 stats) or 2 (DNP), append to a temp player list
temp = []
for i in boxscore:
    if len(i.select('td')) == 15 or len(i.select('td')) == 2:
        temp.append(i)

# because the 'temp' list also contains team-level highlist data, we need to remove them
# check if the temp player list is actual player data row (contains no class tags) and append to the recreated boxscore
boxscore = []
for i in temp:
    if i.attrs == {}:
        boxscore.append(i)

#%%
# append individual player's data into players, which is a list of lists
columns = ['.abbr', '.min','.fg','.3pt','.ft','.oreb','.dreb','.reb','.ast','.stl','.blk','.to','.pf','.plusminus','.pts']
players = []
for i in boxscore:
    player = []
    for column in columns:
        try:
            player.append(i.select(column)[0].text)
        except:
            pass
    players.append(player)

#%%
# import into dataframe
df = pd.DataFrame(players)
df.columns = ['name','min','fg','3pt','ft','oreb','dreb','reb','ast','stl','blk','to','pf','+/-','pts']
df = df.set_index('name')

#%%
# convert str to int
num_columns = ['min','oreb','dreb','reb','ast','stl','blk','to','pf','+/-','pts']
df.fillna(value=np.nan, inplace=True)
for col in num_columns:
    df[col] = pd.to_numeric(df[col])
df #display the final df
