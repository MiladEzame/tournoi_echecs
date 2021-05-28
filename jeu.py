from model import Player, Tournament, Round

if __name__ == "__main__":
    player1 = Player("Ezame", "Milad", "20/01/1994", "M")
    tournament = Tournament("Tournoi2", "Paris", "30/03/2022")
    round = Round()
    player1.ranking(5)
    print(player1.ranking)
    # tester tous les getters et les setters
