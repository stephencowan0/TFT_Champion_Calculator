# Creates the dictionary of all commons, setting availibility to 29
commons = {}
common_file = open("champion_data/commons.csv", "r")
common_list = common_file.readlines()
for champion in common_list:
    champion = champion.rstrip()
    commons[champion] = 29
print(commons)

# Creates the dictionary of all uncommons, setting availibility to 22
uncommons = {}
uncommon_file = open("champion_data/uncommons.csv", "r")
uncommon_list = uncommon_file.readlines()
for champion in uncommon_list:
    champion = champion.rstrip()
    uncommons[champion] = 22
print(uncommons)

# Creates the dictionary of all rares, setting availibility to 18
rares = {}
rare_file = open("champion_data/rares.csv", "r")
rare_list = rare_file.readlines()
for champion in rare_list:
    champion = champion.rstrip()
    rares[champion] = 18
print(rares)

# Creates the dictionary of all epics, setting availibility to 12
epics = {}
epic_file = open("champion_data/epics.csv", "r")
epic_list = epic_file.readlines()
for champion in epic_list:
    champion = champion.rstrip()
    epics[champion] = 12
print(epics)

# Creates the dictionary of all legendaries, setting availibility to 10
legendaries = {}
legendarie_file = open("champion_data/legendaries.csv", "r")
legendarie_list = legendarie_file.readlines()
for champion in legendarie_list:
    champion = champion.rstrip()
    legendaries[champion] = 10
print(legendaries)
