from views import ViewMenu, ViewPlayers, ViewTournament
from model import Tournament, Player, Match, Round
from tinydb import TinyDB
db = TinyDB("db.json")
players_table = db.table("players")
tournaments_table = db.table("tournaments")


class UserManagement:
    def __init__(self):
        self._players = []
        self._player = Player(first_name="", last_name="",
                              date_birth="11/11/1111")

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
        for new_player in range(1, 3):
            ViewPlayers.player_info(self.player)
            new_player = Player(self.player.first_name, self.player.last_name,
                                self.player.date_birth)
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
        PairManagement.generate_pairs(self, self._players)

    def view_players(self):
        """
            Shows players saved in database
        """
        charge = ChargeState()
        charge.charge_player()
        # ViewPlayers.view_players_info(self._players)

    def player_from_file(self):
        """
            Creates players from a file (random_players.txt)
            + saves them in database
        """
        players = [line.split(';') for line in open("random_players.txt")]
        save = SaveState()
        players_table.truncate()
        # print(players)
        i = 1
        new_players = []
        for lists in players:
            all_players = Player(lists[0], lists[1], lists[2])
            all_players.gender = lists[3]
            all_players.ranking = i
            new_players.append(all_players)
            serialized_player = {
                "first_name": all_players.first_name,
                "last_name": all_players.last_name,
                "date_birth": all_players.date_birth,
                "gender": all_players.gender,
                "ranking": all_players.ranking
            }
            i = i + 1
            save.save_player(serialized_player)
        PairManagement.generate_pairs(self, new_players)
        return new_players


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

    def view_tournament_info(self):
        """
            Charges tournament info in the database
        """
        charge = ChargeState()
        charge.charge_tournament()


class RoundManagement():
    def __init__(self):
        self._matchs = []
        self._round = Round()

    @property
    def matchs(self):
        return self._matchs

    @property
    def round(self):
        return self._round

    @matchs.setter
    def matchs(self, new_matchs):
        self._matchs = new_matchs

    @round.setter
    def round(self, new_round):
        self._round = new_round

    def round_naming(self, number):
        self.round.name = "Round {}".format(number)

    def add_score(self):
        pass

    def results_input(self, matchs):
        """
            Allows us to set the winner of a match in a
            given round and adds points accordingly
        """
        for match in matchs:
            results = input("""
            Who won this round ?
            1: Player {}  |  2: Player {}  |  3: Tie
            """)
            if results == 1:
                pass
            elif results == 2:
                pass
            else:
                pass


class PairManagement:
    def __init__(self):
        self._match = Match()
        self._all_players = []

    @property
    def all_players(self):
        return self._all_players

    @all_players.setter
    def all_players(self, all_new_players):
        self._all_players = all_new_players

    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, new_match):
        self._match = new_match

    def generate_pairs(self, all_players):
        """
            Generate the pair of players to run the tournament
            the pairs are generated with the swiss sort method
        """
        lenght = len(all_players)
        middle_index = lenght//2
        first_half = all_players[:middle_index]
        second_half = all_players[middle_index:]
        print("Players on first group : {}".format(first_half))
        print("Players on second group : {}".format(second_half))

    def sort_players_ranking(self, middle_index, first_half, second_half):
        """
            Sort players according to their rankings
            NEEDS TO BE DONE WITH MATCH OBJECT SO NOT USED.
        """
        all_pairs = []
        i = 0
        score = 0
        while i < middle_index:
            pair_player = ((first_half[i], score),
                           (second_half[i], score))
            i = i + 1
            all_pairs.append(pair_player)
        print("\nHere are the pairs generated :")
        for pairs in all_pairs:
            print(pairs)
        [print(x[0][1]) for x in all_pairs]
        [print(x[1][1]) for x in all_pairs]

    def sort_players_points(self):
        pass


class MenuManagement:
    tourney = TournamentManagement()
    players = UserManagement()

    def main_menu(self):
        """
            Shows main menu in an infinite loop to be able to choose
            between the different options until 0 is pressed
        """
        choice = 1
        print("Hello and Welcome to The Annual Chess tournament !")
        while choice != 0:
            choice = ViewMenu.Starting_Menu()
            if choice == 1:
                self.tourney.create_new_tournament()
                self.players.player_from_file()
            elif choice == 2:
                self.tourney.create_new_tournament()
                self.players.create_players()
            elif choice == 3:
                self.players.view_players()
            elif choice == 4:
                self.tourney.view_tournament_info()
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 0:
                print("You chose to leave the tournament management. GoodBye.")
                exit
            else:
                print("You didn't make a valid choice.")
                raise TypeError("Must be a valid number")


class ScoreManagement:
    pass


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
        tournaments_table.insert(serialized_tournament)


class ChargeState:
    def charge_player(self):
        """
            Load players in the database
        """
        for player in players_table:
            print(player)

    def charge_tournament(self):
        """
            Load players in the database
        """
        for tourney in tournaments_table:
            print(tourney)
