from controller import MenuManagement


if __name__ == "__main__":
    """"
    new_players = UserManagement()
    # all_players = new_players.create_players()
    new_players.player_from_file()
    new_players.view_players()
    # pairs = view_players.player_from_file()
    # new_players.generate_pairs(pairs)
    user = TournamentManagement()
    user.create_new_tournament()
    user.view_tournament_info()
    """
    # FAIRE LES METHODES DE TRI
    # REGLER LE PB DE RANKING DANS LE 2E MENU (loaded)
    # AFFICHAGE DES ROUNDS PLUS PROPREMENT SI POSSIBLE
    # GERER LES EXCEPTIONS
    menu = MenuManagement()
    menu.main_menu()
