from model import Player
from controller import UserManagement

if __name__ == "__main__":
    player1 = Player("Ezame", "Milad", "20/01/1993")
    print(player1.ranking)
    player1.ranking = 14
    print(player1.ranking)

    new_players = UserManagement()
    new_players.create_players()
    new_players.view_players()
    """
    user = TournamentManagement()
    user.create_new_tournament()
    user.view_tournament_info()
    """
