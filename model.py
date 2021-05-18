from datetime import datetime


class Player:

    def __init__(self, first_name, last_name, date_of_birth, gender):
        """
            Constructor, creating a new player
        """
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y")
        # enregister sous format date
        self._gender = gender
        self.ranking = 0
        print("Le joueur suivant a été ajouté :\n")
        print(f'''First Name: {self._first_name}       Last Name: {self._last_name}
        \nDate of birth: {self._date_of_birth}   Gender: {self._gender}
        \nRanking: {self.ranking}
              ''')
        # bonne pratique pour des attributs non variables : @property

        @property
        def first_name(self):
            return self.first_name

        @property
        def last_name(self):
            return self.last_name

        @property
        def date_of_birth(self):
            return self.date_of_birth

        @property
        def gender(self):
            return self.gender

        @property
        def ranking_getter(self):
            return self.ranking

        @property
        def ranking_setter(self, new_ranking):
            try:
                if self.ranking >= 0:
                    self.ranking = new_ranking
                else:
                    raise ValueError
            except ValueError:
                print("Ranking needs to be a positive number !")


class Round:

    def __init__(self):
        """
            Constructor, creating a new round
        """
        self._matchs = []
        self._players = []
        self._resultats = []
        self._match = {self._players, self._resultats}
        print("Round 1 !\n")

        @property
        def matchs_getter(self):
            return self.matchs

        @property
        def players_getter(self):
            return self.players

        @property
        def resultats_getter(self):
            return self.resultats

        @property
        def match_getter(self):
            return self.match

        @property
        def resultats_setter(self, new_resultats):
            self.resultats = new_resultats

        @property
        def players_setter(self, new_players):
            self.playesr = new_players

        @property
        def match_setter(self, new_match):
            self.match = new_match


class Tournament:
    def __init__(self, name, place, tour_date):
        """
            Constructor, creating a new tournament
        """
        self._name = name
        self._place = place
        self._tour_date = datetime.strptime(tour_date, "%d/%m/%Y")
        self._number_of_rounds = 4
        self._rounds = []
        self._players = []
        self._time_control = ""
        print("Le tournoi a débuté !\n")

        @property
        def name_getter(self):
            return self._name

        @property
        def place_getter(self):
            return self._place

        @property
        def date_getter(self):
            return self._tour_date

        @property
        def rounds_getter(self):
            return self._rounds

        @property
        def players_getter(self):
            return self._players

        @property
        def time_control_getter(self):
            return self._time_control

        @property
        def rounds_setter(self, new_rounds):
            self._rounds = new_rounds

        @property
        def players_setter(self, players):
            self._players = players

        @property
        def time_control_setter(self):
            choice = input("What kind of game would you like to play ?")
            print("1 = Bullet / 2 = Blitz / 3 = Quick Move")
            if choice == 1:
                return "Bullet Game !"
            elif choice == 2:
                return "Blitz Game !"
            else:
                return "Quick move Game !"
