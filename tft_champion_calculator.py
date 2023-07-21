import numpy as np
import pandas as pd

# Creates the levels dataframe
dfLevels = pd.read_csv("levels.csv")
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):print(dfLevels)

# Creates the dictionary of all commons, setting availibility to 29
commons = {}
common_file = open("champion_data/commons.csv", "r")
common_list = common_file.readlines()
for champion in common_list:
    champion = champion.rstrip()
    commons[champion] = 29
common_file.close()
common_count = len(commons)

# Creates the dictionary of all uncommons, setting availibility to 22
uncommons = {}
uncommon_file = open("champion_data/uncommons.csv", "r")
uncommon_list = uncommon_file.readlines()
for champion in uncommon_list:
    champion = champion.rstrip()
    uncommons[champion] = 22
uncommon_file.close()
uncommon_count = len(uncommons)

# Creates the dictionary of all rares, setting availibility to 18
rares = {}
rare_file = open("champion_data/rares.csv", "r")
rare_list = rare_file.readlines()
for champion in rare_list:
    champion = champion.rstrip()
    rares[champion] = 18
rare_file.close()
rare_count = len(rares)

# Creates the dictionary of all epics, setting availibility to 12
epics = {}
epic_file = open("champion_data/epics.csv", "r")
epic_list = epic_file.readlines()
for champion in epic_list:
    champion = champion.rstrip()
    epics[champion] = 12
epic_file.close()
epic_count = len(epics)

# Creates the dictionary of all legendaries, setting availibility to 10
legendaries = {}
legendarie_file = open("champion_data/legendaries.csv", "r")
legendarie_list = legendarie_file.readlines()
for champion in legendarie_list:
    champion = champion.rstrip()
    legendaries[champion] = 10
legendarie_file.close()
legendarie_count = len(legendaries)

# Create a master dictionary holding all five rarities, thus the data for every champion
master_dictionary = {"commons": commons, "uncommons": uncommons, "rares": rares,
                     "epics": epics, "legendaries": legendaries}

# Read the number of each champion taken from the champions_taken file
# And use this to calculate how much of each champion is left currently
champions_taken_file = open("champions_taken.csv", "r")
champions_taken_list = champions_taken_file.readlines()
total_champion_spot = 0

# Calculates how many of each common are left
current_rarity = 0
while current_rarity < common_count:
    current_line_of_data = champions_taken_list[total_champion_spot].rstrip().split(
        ',')
    commons[current_line_of_data[0]] -= int(current_line_of_data[1])
    current_rarity += 1
    total_champion_spot += 1

# Calculates how many of each uncommon are left
current_rarity = 0
while current_rarity < uncommon_count:
    current_line_of_data = champions_taken_list[total_champion_spot].rstrip().split(
        ',')
    uncommons[current_line_of_data[0]] -= int(current_line_of_data[1])
    current_rarity += 1
    total_champion_spot += 1

# Calculates how many of each rare are left
current_rarity = 0
while current_rarity < rare_count:
    current_line_of_data = champions_taken_list[total_champion_spot].rstrip().split(
        ',')
    rares[current_line_of_data[0]] -= int(current_line_of_data[1])
    current_rarity += 1
    total_champion_spot += 1

# Calculates how many of each epic are left
current_rarity = 0
while current_rarity < epic_count:
    current_line_of_data = champions_taken_list[total_champion_spot].rstrip().split(
        ',')
    epics[current_line_of_data[0]] -= int(current_line_of_data[1])
    current_rarity += 1
    total_champion_spot += 1

# Calculates how many of each legendarie are left
current_rarity = 0
while current_rarity < legendarie_count:
    current_line_of_data = champions_taken_list[total_champion_spot].rstrip().split(
        ',')
    legendaries[current_line_of_data[0]] -= int(current_line_of_data[1])
    current_rarity += 1
    total_champion_spot += 1

# Get user input for their current level
level = int(input("What is your current level?: "))
level_odds = dfLevels.loc[dfLevels['level'] == level]
level_odds = level_odds.to_dict(orient='list')

# Get user input for what rarity they want to see
user_rarity = input("What rarity are you looking for?: ")
level_odds = int(level_odds[user_rarity][0])
if (user_rarity == "legendary"):
    user_rarity = "legendarie"
user_rarity = master_dictionary[(user_rarity+'s')]
# Get user input for what champion they want to see
user_champion = input("What champion are you looking for?: ")

# Calculate the odds of getting a users desired champion
total_in_current_rarity = 0
for champion in user_rarity:
    total_in_current_rarity += int(user_rarity[champion])
odds = user_rarity[user_champion]/total_in_current_rarity
odds = odds*(level_odds/100)*5
odds = round(odds*100, 2)

# Prints the output to the user
print(
    f"For each reroll, the odds of getting {user_champion} at level {level} are currently {odds}%")
