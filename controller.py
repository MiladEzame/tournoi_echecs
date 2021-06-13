from views import ViewTournament
from model import Player, Tournament


class System:
    def __init__(self, tournament):
        self._all_players = []
        self._tournament = tournament

    @property
    def all_players(self):
        return self._all_players

    @property
    def tournament(self):
        return self._tournament

    @all_players.setter
    def all_players(self, new_players):
        self._all_players = new_players

    @tournament.setter
    def tournament(self, new_tournament):
        self._tournament = new_tournament

    def create_new_tournament(self, tournament):
        tournament = Tournament()
        ViewTournament.tournament_info()
        return tournament

    def create_players(self):
        for self.players in range(1, 9):
            self.players = Player()
            self.all_players.append(self.players)
        return self.all_players
