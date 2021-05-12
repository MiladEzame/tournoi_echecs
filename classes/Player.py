class Player:

    def __init__(self, fname, lname, date_of_birth, gender, ranking):
        """
            Constructor, creating a new player
        """
        self.fname = fname
        self.lname = lname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = abs(ranking)
        print("Le joueur suivant a été ajouté :\n")
        print(f'''First Name: {self.fname}           Last Name: {self.lname}
        \nDate of birth: {self.date_of_birth}   Gender: {self.gender}
        \nRanking: {self.ranking}
              ''')
