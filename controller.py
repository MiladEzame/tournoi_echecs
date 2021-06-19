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


class ScoreManagement:
    pass


class SaveState:
    pass


class ChargeState:
    pass
