from model import Tournament
# from model import Match, Player, Tournament, Round
from controller import Controller

if __name__ == "__main__":
    tournament = Tournament()
    controller = Controller(tournament)
    controller.create_new_tournament(tournament)
