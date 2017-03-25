import csv
f = open("nfl_suspensions_data.csv", 'r')
csvreader = csv.reader(f)
nfl_suspensions = list(csvreader)
nfl_suspensions=nfl_suspensions[1:]

years={}
for row in nfl_suspensions:
    row_year= row[5]
    if row_year in years:
        years[row_year] = years[row_year]+1
    else:
        years[row_year] = 1
print(years)

unique_teams=[]
for row in nfl_suspensions:
    team=row[1]
    unique_teams.append(team)
unique_teams=set(unique_teams)

unique_games=set([row[2] for row in nfl_suspensions])
