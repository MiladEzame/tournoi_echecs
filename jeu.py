from controller import UserManagement


if __name__ == "__main__":
    new_players = UserManagement()
    all_players = new_players.create_players()
    new_players.view_players()
    """
    user = TournamentManagement()
    user.create_new_tournament()
    user.view_tournament_info()
    """
