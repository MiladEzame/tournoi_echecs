from views import ViewMenu, ViewPairs, ViewPlayers, ViewTournament
from model import Tournament, Player, Match, Round
from tinydb import TinyDB
import os
db = TinyDB("db.json")
players_table = db.table("players")
tournaments_table = db.table("tournaments")
round_table = db.table("rounds")


class UserManagement:
    def __init__(self):
        self._players = []
        self._player = Player()
        self.match = Match()
        self.round = Round()

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, new_players):
        self._players = new_players

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, new_player):
        self._player = new_player

    def create_players(self):
        """
            Creates players by typing their informations
            + saves them in the Database
        """
        i = 1
        save = SaveState()
        players_table.truncate()
        for new_player in range(1, 9):
            ViewPlayers.player_info(self.player)
            new_player = Player()
            new_player.first_name = self.player.first_name
            new_player.last_name = self.player.last_name
            new_player.date_birth = self.player.date_birth
            new_player.gender = self.player.gender
            new_player.ranking = i
            i = i + 1
            self.players.append(new_player)
            serialized_player = {
                "first_name": new_player.first_name,
                "last_name": new_player.last_name,
                "date_birth": new_player.date_birth,
                "gender": new_player.gender,
                "ranking": new_player.ranking
            }
            save.save_player(serialized_player)
        return self.players

    def view_players(self, players):
        """
            Shows players saved in database
        """
        ViewPlayers.view_players_info(players)

    def charging_players(self):
        """
            Shows players saved in database
        """
        charge = ChargeState()
        charge.charge_player()

    def player_from_file(self):
        """
            Creates players from a file (random_players.txt)
            + saves them in database
        """
        players_file = [line.split(';') for line in open("random_players.txt")]
        save = SaveState()
        players_table.truncate()
        i = 1
        for lists in players_file:
            all_players = Player()
            all_players.first_name = lists[0]
            all_players.last_name = lists[1]
            all_players.date_birth = lists[2]
            all_players.gender = lists[3]
            all_players.ranking = i
            self.players.append(all_players)
            serialized_player = {
                "first_name": all_players.first_name,
                "last_name": all_players.last_name,
                "date_birth": all_players.date_birth,
                "gender": all_players.gender,
                "ranking": all_players.ranking
            }
            i = i + 1
            save.save_player(serialized_player)
        return self.players

    def change_ranking(self, all_players):
        for player in all_players:
            print(player)
        change = int(input("""
        What player s ranking would you like to change ?
        Enter the number according the current ranking of the player.
        """))
        for i in range(1, 9):
            if change == i:
                return all_players[i-1]
            else:
                pass

    def set_ranking(self, all_players):
        player = UserManagement.change_ranking(self, all_players)
        new_ranking = int(input("What is the new ranking for this player?"))
        player.ranking = new_ranking


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
        """
            creates new tournament and save it in the database
        """
        save = SaveState()
        ViewTournament.tournament_input(self.tournament)
        serialized_tournament = {
            "Name": self.tournament.name,
            "Place": self.tournament.place,
            "Date": self.tournament.tour_date
        }
        save.save_tournament(serialized_tournament)

    def charging_tournament(self):
        """
            Charges tournament info in the database
        """
        charge = ChargeState()
        charge.charge_tournament()

    def view_tournament_info(self):
        """
            Charges tournament info in the database
        """
        charge = ChargeState()
        charge.view_charged_tournament()


class RoundManagement():
    def __init__(self):
        self._matchs = []
        self._match = Match()
        self._round = Round()
        self._players = []

    @property
    def matchs(self):
        return self._matchs

    @property
    def round(self):
        return self._round

    @property
    def match(self):
        return self._match

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, new_players):
        self._players = new_players

    @matchs.setter
    def matchs(self, new_matchs):
        self._matchs = new_matchs

    @match.setter
    def match(self, new_match):
        self._match = new_match

    @round.setter
    def round(self, new_round):
        self._round = new_round

    def round_naming(self, number):
        self.round.name = "Round {}".format(number)

    def saving_round(self, match, nb_rounds, all_players):
        """
            creates new tournament and save it in the database
            Changing the Players in string format to be able to save
            Then changing them back to Player format
        """
        save = SaveState()
        for players in match.round:
            players[0][0] = str(players[0][0])
            players[1][0] = str(players[1][0])
        serialized_round = {
            "Name": "Round " + str(nb_rounds),
            "Pairs": match.round,
        }
        save.save_round(serialized_round)
        nb = 0
        for players in self.match.round:
            players[0][0] = all_players[nb]
            players[1][0] = all_players[nb+1]
            nb = nb + 2
        return serialized_round

    def charging_round(self):
        """
            Charges tournament info in the database
        """
        charge = ChargeState()
        charge.charge_round()

    def view_round_info(self):
        """
            Charges tournament info in the database
        """
        charge = ChargeState()
        charge.view_charged_round()

    def results_input(self, all_players, nb, rd):
        """
            Allows us to set the winner of a match in a
            given round and adds points accordingly
            or match in matchs:
        """
        results = input("""
        Who won this round ?
        {}  |  {}  |  Tie : 3
        """.format(all_players[nb], all_players[nb+1]))
        if int(results) == 1:
            self.match.round[rd][0][1] += 1
        elif int(results) == 2:
            self.match.round[rd][1][1] += 1
        elif int(results) == 3:
            self.match.round[rd][0][1] += 0.5
            self.match.round[rd][1][1] += 0.5
        else:
            print("You didn't make a valid choice.")
            input("\nPress any key to return to menu.")
            MenuManagement.round_menu(self, all_players)


class PairManagement:
    def __init__(self):
        self._match = Match()
        self._players = []
        self._scores = []
        self._round = Round()

    @property
    def players(self):
        return self._players

    @property
    def match(self):
        return self._match

    @property
    def scores(self):
        return self._scores

    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, new_round):
        self._round = new_round

    @scores.setter
    def scores(self, new_scores):
        self._scores = new_scores

    @players.setter
    def all_players(self, all_new_players):
        self._players = all_new_players

    @match.setter
    def match(self, new_match):
        self._match = new_match

    def generate_pairs(self, all_players):
        """
            Generate the pair of players to run the tournament,
            the pairs are generated with the swiss sort method
        """
        player = 0
        for i in range(0, 4):
            self.match.unique_match = ([all_players[player], 0],
                                       [all_players[player+1], 0])
            self.match.round.append(self.match.unique_match)
            player = player + 2
        ViewPairs.view_generated_pairs(self.match.round)
        return self.match.round

    def start_round(self, all_players):
        """
            Creates 4 rounds for every tournament and all the
            methods will be called from this one.
            This will generate 4 rounds in which pairs will be
            sorted and generated according to their ranks/scores
        """
        nmb_of_rounds = 1
        self.match.round = PairManagement.generate_pairs(self, all_players)
        round_table.truncate()
        for nmb_of_rounds in range(1, 5):
            print("\nROUND {}".format(nmb_of_rounds))
            rd = 0
            nb = 0
            print(len(self.match.round))
            while rd < len(self.match.round):
                print("MATCH {}".format(rd+1))
                print(self.match.round[rd])
                RoundManagement.results_input(
                    self, all_players, nb, rd)
                nb = nb + 2
                rd = rd + 1
            RoundManagement.saving_round(self, self.match,
                                         nmb_of_rounds, all_players)
            MenuManagement.round_menu(self, all_players)

    def sort_players_ranking(self):
        pass

    def sort_players_points(self):
        pass


class MenuManagement:
    tourney = TournamentManagement()
    players = UserManagement()
    match = Match()
    round = Round()

    def main_menu(self):
        """
            Shows main menu in an infinite loop to be able to choose
            between the different options until 0 is pressed
        """
        choice = 1
        print("Hello and Welcome to The Chess tournament !")
        while choice != 0:
            choice = int(ViewMenu.starting_menu())
            if choice == 1:
                self.tourney.create_new_tournament()
                self.players.player_from_file()
                input("\nPress any key to return to menu.")
            elif choice == 2:
                self.tourney.create_new_tournament()
                self.players.create_players()
                input("\nPress any key to return to menu.")
            elif choice == 3:
                os.system("cls")
                self.players.view_players(self.players.players)
                input("\nPress any key to return to menu.")
            elif choice == 4:
                os.system("cls")
                self.tourney.view_tournament_info()
                input("\nPress any key to return to menu.")
            elif choice == 5:
                os.system("cls")
                if self.players.players == []:
                    input("PLEASE CREATE PLAYERS FIRST\nEnter to continue")
                    MenuManagement.main_menu(self)
                PairManagement.start_round(self.players, self.players.players)
                input("\nPress any key to return to menu.")
            elif choice == 6:
                os.system("cls")
                self.players.view_players(self.players.players)
                self.tourney.view_tournament_info()
                RoundManagement.view_round_info(self)
                MenuManagement.charged_round_menu(self, self.players.players)
            elif choice == 0:
                print("You chose to leave the tournament management. GoodBye.")
                break
            else:
                print("You didn't make a valid choice.")
                input("\nPress any key to return to menu.")
                self.main_menu()

    def round_menu(self, all_players):
        choice = 1
        while choice != 0:
            choice = ViewMenu.round_menu()
            if choice == 1:
                ViewPlayers.view_pairs(self, self.match.round)
                input("\nPress any key to return to menu.")
            elif choice == 2:
                UserManagement.set_ranking(self, all_players)
            elif choice == 3:
                os.system("cls")
                players_table.all()
                ViewPlayers.view_players_info(all_players)
                input("\nPress any key to return to menu.")
            elif choice == 4:
                os.system("cls")
                ViewPlayers.view_players_points(self, self.match.round)
                input("\nPress any key to return to menu.")
            elif choice == 5:
                os.system("cls")
                # RoundManagement.saving_round(self, self.match.round)
                input("\nRound Saved. Press any key to return to menu.")
            elif choice == 6:
                os.system("cls")
                ChargeState.view_charged_round(self)
                input("\nPress any key to return to menu.")
            elif choice == 7:
                os.system("cls")
                MenuManagement.main_menu(self)
            else:
                break

    def charged_round_menu(self, all_players):
        choice = 1
        while choice != 0:
            choice = ViewMenu.round_menu()
            if choice == 1:
                os.system("cls")
                ChargeState.charge_tournament(self)
                ChargeState.view_charged_pairs_round(self)
                input("\nPress any key to return to menu.")
            elif choice == 2:
                ChargeState.charge_player(self)
                UserManagement.set_ranking(self, all_players)
            elif choice == 3:
                os.system("cls")
                ChargeState.view_charged_player(self)
                ViewPlayers.view_players_info(all_players)
                input("\nPress any key to return to menu.")
            elif choice == 4:
                os.system("cls")
                ChargeState.view_charged_player_points(self)
                input("\nPress any key to return to menu.")
            elif choice == 5:
                os.system("cls")
                input("\nRound already Saved. Press any key to return to menu")
            elif choice == 6:
                os.system("cls")
                ChargeState.view_charged_round(self)
                input("\nPress any key to return to menu.")
            elif choice == 7:
                os.system("cls")
                MenuManagement.main_menu(self)
            else:
                break


class SaveState:
    def save_player(self, serialized_player):
        """
            Save players in the database
        """
        players_table.insert(serialized_player)

    def save_tournament(self, serialized_tournament):
        """
            Save tournament in the database
        """
        tournaments_table.truncate()
        tournaments_table.insert(serialized_tournament)

    def save_round(self, serialized_round):
        """
            Save players in the database
        """
        round_table.insert(serialized_round)


class ChargeState:
    def view_charged_player(self):
        """
            Load players in the database
        """
        players_table.all()
        ViewPlayers.view_players_loaded_table(self, players_table)

    def view_charged_player_points(self):
        """
            Load players in the database
        """
        round_table.all()
        ViewPlayers.view_players_points_table(self, round_table)

    def view_charged_tournament(self):
        """
            Load players in the database
        """
        tournaments_table.all()
        for tournament in tournaments_table:
            print(tournament)

    def view_charged_round(self):
        """
            Load rounds in the database
        """
        round_table.all()
        for rounds in round_table:
            print(rounds)

    def view_charged_pairs_round(self):
        round_table.all()
        ViewPairs.view_loaded_pairs_table(self, round_table)

    def charge_player(self):
        """
            Load players in the database
        """
        players_table.all()
        for player in players_table:
            print(player)

    def charge_tournament(self):
        """
            Load players in the database
        """
        tournaments_table.all()

    def charge_round(self):
        """
            Load rounds in the database
        """
        round_table.all()
