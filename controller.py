from views import ViewPlayers, ViewTournament
from model import Tournament, Player


class UserManagement:
    def __init__(self):
        self._players = []
        self._player = Player(first_name="", last_name="",
                              date_birth="11/11/1111")

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, new_players):
        self._players = new_players

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, new_player):
        self._player = new_player

    def create_players(self):
        i = 1
        for new_player in range(1, 3):
            ViewPlayers.player_info(self.player)
            new_player = Player(self.player.first_name, self.player.last_name,
                                self.player.date_birth)
            new_player.gender = self.player.gender
            new_player.ranking = i
            i = i + 1
            self.players.append(new_player)
        PairManagement.generate_pairs(self, self._players)

    def view_players(self):
        ViewPlayers.view_players_info(self._players)

    def player_from_file(self):
        players = [line.split(';') for line in open("random_players.txt")]
        # print(players)
        i = 1
        new_players = []
        for lists in players:
            all_players = Player(lists[0], lists[1], lists[2])
            all_players.gender = lists[3]
            all_players.ranking = i
            new_players.append(all_players)
            i = i + 1
        return new_players


class TournamentManagement:
    def __init__(self):
        self._tournament = Tournament()

    @property
    def tournament(self):
        return self._tournament

    @tournament.setter
    def tournament(self, new_tournament):
        self._tournament = new_tournament

    def create_new_tournament(self):
        ViewTournament.tournament_input(self.tournament)

    def view_tournament_info(self):
        ViewTournament.view_tournament_info(self.tournament)


class PairManagement:

    def __init__(self):
        self._all_players = []

    @property
    def all_players(self):
        return self._all_players

    @all_players.setter
    def all_players(self, all_new_players):
        self._all_players = all_new_players

    def generate_pairs(self, all_players):
        lenght = len(all_players)
        middle_index = lenght//2
        first_half = all_players[:middle_index]
        second_half = all_players[middle_index:]
        print("Players ranked from 1 to 4 : {}".format(first_half))
        print("Players ranked from 5 to 8 : {}".format(second_half))

    def sort_pairs(self):
        pass


class ScoreManagement:
    pass


class SaveState:
    pass


class ChargeState:
    pass
