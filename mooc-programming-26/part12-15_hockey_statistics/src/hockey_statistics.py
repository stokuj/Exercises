# Write your solution here
import json

class Player:
    def __init__(self, name :str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self._name = name
        self._nationality = nationality
        self._assists = assists
        self._goals = goals
        self._penalties = penalties
        self._team = team
        self._games = games
        
    def __str__(self):
        return f"{self._name:<20} {self._team:<4} {self._goals:>2} + {self._assists:>2} = {self.points():>3}"
        
    def name(self):
        return self._name
    
    def nationality(self):
        return self._nationality
    
    def assists(self):
        return self._assists
    
    def goals(self):
        return self._goals
    
    def penalties(self):
        return self._penalties
    
    def team(self):
        return self._team
    
    def games(self):
        return self._games
    
    def points(self):
        return self._goals + self._assists

class PlayerStatistics:
    def __init__(self):
        self._players = {} #name : Player (object)

    def add_player(self, name :str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        player = Player(name, nationality, assists, goals, penalties, team, games)
        self._players[name] = player
        
    def load_data_from_file(self, file_name: str):
        with open(file_name) as file:
            stats = json.load(file)
            for player in stats:
                self.add_player(
                    player['name'],
                    player['nationality'],
                    player['assists'],
                    player['goals'],
                    player['penalties'],
                    player['team'],
                    player['games']
                )
        size = len(self._players)
        print(f'read the data of {size} players')

    def search_for_player(self, name: str) -> Player:
        if name in self._players:
            return self._players[name]
        return None
    
    def get_countries(self):
        for nationality in sorted(set([self._players[player].nationality() for player in self._players])):
            print (nationality)
        
    def get_teams(self):
        for team in sorted(set([self._players[player].team() for player in self._players])):
            print (team)
            
    def get_players_in_team(self, name_of_team: str) -> list:
        players = sorted(
            [self._players[player] for player in self._players if self._players[player].team() == name_of_team],
            key=lambda player: player.points(),
            reverse=True,
        )
        for player in players:
            print(player)
    
    def get_players_in_country(self, name_of_country: str) -> list:
        players = sorted(
            [self._players[player] for player in self._players if self._players[player].nationality() == name_of_country],
            key=lambda player: player.points(),
            reverse=True,
        )
        for player in players:
            print(player)
    
    def most_points(self, n: int) -> list:
        players = sorted(
            [self._players[player] for player in self._players],
            key=lambda player: (player.points(), player.goals()),
            reverse=True,
        )
        for i in range(n):
            print(players[i])

    def most_goals(self, n: int) -> list:
        players = sorted(
            [self._players[player] for player in self._players],
            key=lambda player: (player.goals(), -player.games()),
            reverse=True,
        )
        for i in range(n):
            print(players[i])

    
class App:
    def __init__(self):
        self._player_statistics = PlayerStatistics()
        
    def help(self):
        print('')
        print('commands:')
        print('0 quit')
        print('1 search for player')
        print('2 teams')
        print('3 countries')
        print('4 players in team')
        print('5 players from country')
        print('6 most points')
        print('7 most goals')
        
    def run(self):
        file_name = input('file name: ')
        self._player_statistics.load_data_from_file(file_name)
        self.help()

        while True:
            print('')
            command = input('command: ')
            if command == '0':
                break
            if command == '1':
                player_name = input('name: ')
                print(self._player_statistics.search_for_player(player_name))
            elif command == '2':
                self._player_statistics.get_teams()
            elif command == '3':
                self._player_statistics.get_countries()
            elif command == '4':
                name_of_team = input('team: ')
                self._player_statistics.get_players_in_team(name_of_team)
            elif command == '5':
                name_of_country = input('country: ')
                self._player_statistics.get_players_in_country(name_of_country)
            elif command == '6':
                points = int(input('how many: '))
                self._player_statistics.most_points(points)
            elif command == '7':
                goals = int(input('how many: '))
                self._player_statistics.most_goals(goals)
         

    
app = App()
app.run()
