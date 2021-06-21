from views import ViewPlayers, ViewTournament
from model import Tournament


class UserManagement:
    def __init__(self):
        self._player = []

    @property
    def all_players(self):
        return self._player

    @all_players.setter
    def player(self, new_players):
        self._player = new_players

    def create_players(self):
        ViewPlayers.player_info(self._player)
        PairManagement.generate_pairs(self, self._player)

    def view_players(self):
        ViewPlayers.view_players_info(self._player)


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
        print("this is first half {}".format(first_half))
        print("this is second half {}".format(second_half))

    def sort_pairs(self):
        pass


class ScoreManagement:
    pass


class SaveState:
    pass


class ChargeState:
    pass
