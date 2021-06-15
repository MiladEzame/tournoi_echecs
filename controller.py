from views import ViewTournament
from model import Player, Tournament


class UserManagement:
    def __init__(self):
        self._all_players = []

    @property
    def all_players(self):
        return self._all_players

    @all_players.setter
    def all_players(self, new_players):
        self._all_players = new_players

    def create_players(self):
        for self.players in range(1, 9):
            self.players = Player()
            self.all_players.append(self.players)
        return self.all_players


class TournamentManagement:
    def __init__(self):
        self._tournament = ""

    @property
    def tournament(self):
        return self._tournament

    @tournament.setter
    def tournament(self, new_tournament):
        self._tournament = new_tournament

    def create_new_tournament(self, tournament):
        tournament = Tournament()
        ViewTournament.tournament_input(self, tournament)
        return tournament

    def view_tournament_info(self, tournament):
        tournament = Tournament()
        ViewTournament.view_tournament_info(self, tournament)


class ScoreManagement:
    pass


class SaveState:
    pass


class ChargeState:
    pass
