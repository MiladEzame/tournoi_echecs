from controller import UserManagement
from views import ViewPlayers

if __name__ == "__main__":
    new_players = UserManagement()
    all_players = new_players.create_players()
    new_players.view_players()
    view_players = ViewPlayers()
    # pairs = view_players.player_from_file()
    # new_players.generate_pairs(pairs)
    """
    user = TournamentManagement()
    user.create_new_tournament()
    user.view_tournament_info()
    """
