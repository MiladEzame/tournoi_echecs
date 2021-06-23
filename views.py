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
        player.first_name = input(str("Player's first name ?"))
        player.last_name = input(str("Player's last name ?"))
        player.date_birth = input("Date of birth ?")
        player.gender = input(str("Gender ?"))

    @classmethod
    def view_players_info(self, players):
        counter = 1
        for player in players:
            print("\n*******PLAYER N°{}******".format(counter))
            print(player.first_name)
            print(player.last_name)
            print(player.gender)
            print(player.date_birth)
            print(player.ranking)
            counter += 1


class ViewMenu:

    """
    def Menu(choice):
        play = 1
        while play == 1:
            print("Hello and Welcome to The Anual Chess tournament !")
            print("What would you like to do?")
            choice = int(input("To create a tournament and play press 1
            To view the results press 2
            To view the players press 3
            To view the tournament information press 4
            To exit press 0 "))
            if choice == 1:
                new_players = UserManagement()
                new_players.create_players()
            elif choice == 0:
                exit
    """


class ViewRanking:
    pass


class ViewPairs:
    pass


class ViewReports:
    pass
