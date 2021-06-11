from model import Player, Tournament


class Controller:
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
        tournament.name = input("What is the name of the tournament?")
        tournament.place = input("At what place ?")
        tournament.tour_date = input("At what date ?")
        return tournament

    def create_players(self):
        for self.players in range(1, 9):
            self.players = Player()
            self.players.first_name = input(str("Player's first name ?"))
            self.players.last_name = input(str("Player's last name ?"))
            self.players.date_of_birth = input("Date of birth ?")
            self.players.gender = input(str("Gender ?"))
            self.players.ranking = 0
            self.all_players.append(self.players)
        return self.all_players
