from model import Player
from controller import System

if __name__ == "__main__":
    player1 = Player("Ezame", "Milad", "20/01/1993")
    print(player1.ranking)
    player1.ranking = 14
    print(player1.ranking)

    gestion = System()
    gestion.create_new_tournament("Test")
