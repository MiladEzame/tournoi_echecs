from datetime import datetime


class Player:

    def __init__(self):
        """
            Constructor, creating a new player
        """
        self._first_name = ""
        self._last_name = ""
        self._date_birth = datetime.datetime("%d/%m/%Y")
        # enregister sous format date
        self._gender = ""
        self._ranking = 0
        """print("Le joueur suivant a été ajouté :\n")
        print(f'''First Name: {self._first_name}
        Last Name: {self._last_name}
        Date of birth: {self._date_of_birth}   Gender: {self._gender}
        Ranking: {self._ranking}
              ''')
        """
        # bonne pratique pour des attributs non variables : @property

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def date_birth(self):
        return self._date_birth

    @property
    def gender(self):
        return self._gender

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, new_ranking):
        if isinstance(new_ranking, int):
            if new_ranking >= 0:
                self._ranking = new_ranking
            else:
                raise ValueError("Needs to be a positive number !")
        else:
            raise TypeError("Needs to be an integer")


class Round:

    def __init__(self):
        """
            Constructor, creating a new round
        """
        self._matchs = []
        self._players = []
        self._resultats = []
        self._match = (self._players, self._resultats)
        # faire un tuple pour essayer de hasher?

    @property
    def matchs(self):
        return self._matchs

    @property
    def players(self):
        return self._players

    @property
    def resultats(self):
        return self._resultats

    @property
    def match(self):
        return self._match

    @matchs.setter
    def matchs(self, new_matchs):
        self._matchs = new_matchs

    @resultats.setter
    def resultats(self, new_resultats):
        self._resultats = new_resultats

    @players.setter
    def players(self, new_players):
        self._playesr = new_players

    @match.setter
    def match(self, new_match):
        self._match = new_match


class Tournament:
    def __init__(self):
        """
            Constructor, creating a new tournament
        """
        self._name = ""
        self._place = ""
        self._tour_date = ""
        self._number_of_rounds = 4
        self._rounds = []
        self._players = []
        self._time_control = ""

    @property
    def name(self):
        return self._name

    @property
    def place(self):
        return self._place

    @property
    def tour_date(self):
        return datetime.strptime(self._tour_date, "%d/%m/%Y")

    @property
    def rounds(self):
        return self._rounds

    @property
    def players(self):
        return self._players

    @property
    def time_control(self):
        return self._time_control

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @place.setter
    def place(self, new_place):
        self._place = new_place

    @rounds.setter
    def rounds(self, new_rounds):
        self._rounds = new_rounds

    @players.setter
    def players(self, players):
        self._players = players

    @time_control.setter
    def time_control(self):
        choice = input("What kind of game would you like to play ?")
        print("1 = Bullet / 2 = Blitz / 3 = Quick Move")
        if choice == 1:
            return "Bullet Game !"
        elif choice == 2:
            return "Blitz Game !"
        else:
            return "Quick move Game !"


class Match:
    def __init__(self):
        """
            Constructor, creating a new match
        """
        self._players = []
        self._scores = []
        # add player instances
        self._unique_match = (self._players, self._scores)
        # match composed of a list of players, and a list of scores
        self._matchs = []
        print("Le match a débuté !\n")

    @property
    def players(self):
        return self.players

    @property
    def unique_match(self):
        return self._unique_match

    @property
    def matchs(self):
        return self.matchs

    @players.setter
    def players(self, new_players):
        self._players = new_players

    @unique_match.setter
    def match(self, new_match):
        self._match = new_match

    @matchs.setter
    def matchs(self, new_matchs):
        self._matchs = new_matchs
