commons = {}
common_file = open("commons.csv", "r")
common_list = common_file.readlines()
for champion in common_list:
    champion = champion.rstrip()
    commons[champion] = 29
print(commons)
