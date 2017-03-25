#CSV : https://github.com/fivethirtyeight/data/blob/master/nfl-suspensions/nfl-suspensions-data.csv
    
    
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



class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2] 
        self.year = row[5]
third_suspension = Suspension(nfl_suspensions[2])




class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2] 
        try:
            self.year = int(row[5])
        except Exception:
             self.year = 0
    def get_year(self):
        return(self.year)
                
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year() ##23e_year is a int

