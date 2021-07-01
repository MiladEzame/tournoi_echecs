import os


class ViewTournament:

    @classmethod
    def tournament_input(self, tournament):
        """
            Input for the tournament informations
        """
        tournament.name = input("What is the name of the tournament? ")
        tournament.place = input("At what place ? ")
        tournament.tour_date = input("At what date ? ")

    @classmethod
    def view_tournament_info(self, tournament):
        """
            Output of the tournament informations
        """
        print("Name : {}".format(tournament.name))
        print("Place : {}".format(tournament.place))
        print("Date : {}".format(tournament.tour_date))


class ViewPlayers:

    @classmethod
    def player_info(self, player):
        """
            Input for the players informations
        """
        player.first_name = input(str("Player's first name ?"))
        player.last_name = input(str("Player's last name ?"))
        player.date_birth = input("Date of birth ?")
        player.gender = input(str("Gender ?"))

    @classmethod
    def view_players_info(self, players):
        """
            Output for the players informations
        """
        counter = 1
        for player in players:
            print("\n*******PLAYER N°{}******".format(counter))
            print("First Name : {}".format(player.first_name))
            print("Last Name : {}".format(player.last_name))
            print("Gender : {}".format(player.gender))
            print("Date of birth : {}".format(player.date_birth))
            print("Ranking : {}".format(player.ranking))
            counter += 1

    def view_players_points(self, round):
        print("Here are the points of all the players :")
        for pairs in round:
            print(pairs)


class ViewMenu:

    @classmethod
    def starting_Menu(self):
        """
            Choice input for the Main menu
        """
        os.system("cls")
        print("**MAIN MENU **\nWhat would you like to do?")
        choice = input("""
            To create a tournament with random players press 1
            To create a tournament with new players press 2
            To view the players press 3
            To view all the tournaments informations press 4
            To START the tournament press 5
            To exit press 0\n
            Your Choice : """)
        return choice

    @classmethod
    def round_menu(self):
        """
            Choice input for the round menu
        """
        os.system("cls")
        print("**ROUND MENU **\nWhat would you like to do?")
        choice = int(input("""
            To view the pairs press 1
            To change the ranking of a player press 2
            To view the players press 3
            To view the points of the players press 4
            To get to next round press 0\n
            Your Choice : """))
        return choice


class ViewRanking:
    @classmethod
    def rank(self, players):
        print(players)


class ViewPairs:
    @classmethod
    def view_generated_pairs(self, generated_pairs):
        print("Here are the generated pairs :")
        for elt in generated_pairs:
            print(elt)
