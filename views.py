from model import Player


class ViewTournament:

    @classmethod
    # revoir classmethod OPC
    def tournament_input(self, tournament):
        tournament.name = input("What is the name of the tournament? ")
        tournament.place = input("At what place ? ")
        tournament.tour_date = input("At what date ? ")

    @classmethod
    def view_tournament_info(self, tournament):
        print(tournament.name)
        print(tournament.place)
        print(tournament.tour_date)


class ViewPlayers:

    @classmethod
    def player_info(self, player):
        for new_player in range(1, 3):
            first_name = input(str("Player's first name ?"))
            last_name = input(str("Player's last name ?"))
            date_birth = input("Date of birth ?")
            gender = input(str("Gender ?"))
            new_player = Player(first_name, last_name,
                                date_birth)
            new_player.gender = gender
            player.append(new_player)
        return player

    @classmethod
    def view_players_info(self, players):
        counter = 1
        for player in players:
            print(player.first_name)
            print(player.last_name)
            print(player.gender)
            print(player.date_birth)
            print("\n*******PLAYER N°{}******", counter)
            counter += 1


class ViewRanking:
    pass


class ViewPairs:
    pass


class ViewReports:
    pass
