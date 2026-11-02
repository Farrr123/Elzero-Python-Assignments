"""Examples of object-oriented programming concepts."""


class Game:
    """Represent a video game and its details."""

    def __init__(self, name: str, developer: str, year: int, price: float) -> None:
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self) -> float:
        """Convert the game price to Egyptian pounds."""
        return self.price + 730


game_one = Game("Ys", "Falcom", 2010, 50.0)

print(f'Game Name Is "{game_one.name}", ', end="")
print(f'Developer Is "{game_one.developer}", ', end="")
print(f'Release Date Is "{game_one.year}", ', end="")
print(
    f"Price In Egypt Is {game_one.price_in_pounds()} Egyptian Pounds",
    end="",
)

# Needed Output
# Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010",
# Price In Egypt Is 780.0 Egyptian Pounds

print("\n\n" + "#" * 50 + "\n")


class User:
    """Represent a user with personal details."""

    def __init__(self, first_name: str, last_name: str, age: int, gender: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def full_details(self) -> str:
        """Return the user's full details."""
        title = "Mr" if self.gender == "Male" else "Mrs"

        years_to_reach_40 = 40 - self.age

        return (
            f"Hello {title} {self.first_name} {self.last_name[0]}. "
            f"[{years_to_reach_40:02d}] Years To Reach 40"
        )


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())
print(user_two.full_details())

print("\n\n" + "#" * 50 + "\n")


class Message:
    """Demonstrate a class method."""

    @classmethod
    def print_message(cls) -> str:
        """Return a greeting message."""
        return "Hello From Class Message"


print(Message.print_message())

print("\n\n" + "#" * 50 + "\n")


class Games:
    """Represent one game, multiple games, or a game count."""

    def __init__(self, games: str | list[str] | int) -> None:
        self.games = games

    def show_games(self) -> None:
        """Display the stored game information."""
        if isinstance(self.games, str):
            print(f'I Have One Game Called "{self.games}"')

        elif isinstance(self.games, list):
            print("I Have Many Games:")

            for game in self.games:
                print(f"-- {game}")

        else:
            print(f"I Have {self.games} Game.")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()

my_games_names.show_games()

my_games_count.show_games()

print("\n\n" + "#" * 50 + "\n")


class Members:
    """Base class for members with permissions."""

    def __init__(self, name: str, permission: str) -> None:
        self.name = name
        self.permission = permission

    def show_info(self) -> str:
        """Return the member's information."""
        return f"Your Name Is {self.name} And You Are {self.permission}"


class Admins(Members):
    """Represent an admin member."""


class Moderators(Members):
    """Represent a moderator member."""


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
print(member_two.show_info())

print("\n\n" + "#" * 50 + "\n")
