from model import Player
from controller import User_Management

if __name__ == "__main__":
    player1 = Player("Ezame", "Milad", "20/01/1993")
    print(player1.ranking)
    player1.ranking = 14
    print(player1.ranking)

    user = User_Management()
    user.create_new_tournament("Test")
