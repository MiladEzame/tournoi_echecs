from model import Tournament, Player


if __name__ == "__main__":
    player1 = Player()
    player1.first_name("Ezame")
    print(player1.first_name)
    tournament = Tournament()
    print(tournament.name)
