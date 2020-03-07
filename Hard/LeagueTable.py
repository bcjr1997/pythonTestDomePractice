from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        #  -self.standings[player]['score'] means sort the array in descending order (From highest to lowest) based on score
        # self.standings[player]['games_played'] means sort the array in ascending order based on games_played
        sorted_standings = sorted(self.standings, key=lambda player : (-self.standings[player]['score'], self.standings[player]['games_played']))
        return sorted_standings[rank]
      
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))