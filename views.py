class ViewTournament:

    def tournament_input(self, tournament):
        tournament.name = input("What is the name of the tournament?")
        tournament.place = input("At what place ?")
        tournament.tour_date = input("At what date ?")
        """
        print(tournament.name)
        print(tournament.place)
        print(tournament.tour_date)
        """

    def view_tournament_info(self, tournament):
        print(tournament.name)
        print(tournament.place)
        print(tournament.tour_date)


class ViewPlayers:

    def player_info(self, player):
        self.players.first_name = input(str("Player's first name ?"))
        self.players.last_name = input(str("Player's last name ?"))
        self.players.date_of_birth = input("Date of birth ?")
        self.players.gender = input(str("Gender ?"))

    def show_players(self, players):
        for self.players in range(1, 9):
            print(self.players)


class ViewRanking:
    pass


class ViewPairs:
    pass


class ViewReports:
    pass
