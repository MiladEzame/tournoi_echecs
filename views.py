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
        nb = 0
        for pairs in round:
            print("{} has {} points".format(pairs[nb][nb], pairs[nb][1]))
            print("{} has {} points".format(pairs[nb+1][nb], pairs[nb+1][1]))

    def view_players_points_table(self, round):
        print("Here are the points of all the players :")
        nb = 0
        for rounds in round:
            for pairs in rounds.get("Pairs"):
                if nb == 4:
                    break
                print("{} has {} points".format(pairs[0][0], pairs[0][1]))
                print("{} has {} points".format(pairs[1][0], pairs[1][1]))
                nb = nb + 1

    def view_pairs(self, round):
        print("Here are all the pairs:")
        nb = 1
        for pairs in round:
            print("Pair {} : {} vs {}".format(nb, pairs[0][0],
                                              pairs[1][0]))
            nb = nb + 1

    def view_pairs_round(self, round):
        print("Here are all the pairs of the round:")
        for pairs in round:
            print(pairs)

    def view_players_loaded_table(self, players):
        nb = 1
        print("Loaded players :")
        for player in players:
            print("""
        Player {}: {} {} - Date of birth: {} - Gender: {}""".format(
                       nb,
                       player.get("first_name"),
                       player.get("last_name"),
                       player.get("date_birth"),
                       player.get("gender"),).split("\n")[1])
            nb = nb + 1


class ViewMenu:

    @classmethod
    def starting_menu(self):
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
            To Charge the previous tournament press 6
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
            To save the state of the current game press 5
            To charge the state of the past game press 6
            To go back to the main menu press 7
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
        print("Here are the pairs :")
        for elt in generated_pairs:
            print(elt)

    def view_loaded_pairs_table(self, round):
        nb = 0
        print("Here are the pairs :")
        for rounds in round:
            for pairs in rounds.get("Pairs"):
                if nb == 4:
                    break
                print("{} vs {}".format(pairs[0][0], pairs[1][0]))
                nb = nb + 1
