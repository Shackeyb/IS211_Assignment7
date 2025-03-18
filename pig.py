import random

class Die:
    """Represents a six-sided die."""
    def __init__(self, seed=0):
        random.seed(seed)

    def roll(self):
        return random.randint(1, 6)

class Player:
    """Represents a player in the game."""
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_to_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

class Game:
    """Represents the Pig game logic."""
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.die = Die()
        self.current_player_index = 0

    def switch_turn(self):
        """Switch to the next player's turn."""
        self.current_player_index = 1 - self.current_player_index

    def play_turn(self, player):
        """Handles a single player's turn."""
        turn_total = 0
        print(f"\n{player.name}'s turn!")

        while True:
            roll = self.die.roll()
            print(f"{player.name} rolled a {roll}.")

            if roll == 1:
                print("Rolled a 1! No points earned this turn.")
                break
            else:
                turn_total += roll
                print(f"Turn total: {turn_total}, Current score: {player.score}")

                decision = input("Roll again (r) or Hold (h)? ").strip().lower()
                if decision == 'h':
                    player.add_to_score(turn_total)
                    break

    def check_winner(self):
        """Check if any player has won the game."""
        for player in self.players:
            if player.score >= 100:
                print(f"\n{player.name} wins with {player.score} points!")
                return True
        return False

    def start(self):
        """Starts the game loop."""
        print("Welcome to Pig!")
        
        while True:
            current_player = self.players[self.current_player_index]
            self.play_turn(current_player)

            if self.check_winner():
                break

            self.switch_turn()

if __name__ == "__main__":
    game = Game()
    game.start()