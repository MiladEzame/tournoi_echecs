from model import Match, Player, Tournament, Round

if __name__ == "__main__":
    player1 = Player("Ezame", "Milad", "20/01/1994", "M")
    tournament = Tournament("Tournoi2", "Paris", "30/03/2022")
    round = Round()
    match = Match()
    print(player1.first_name)
    print(tournament.name)
    print(round.resultats)
    print(match.unique_match)
    # tester tous les getters et les setters
