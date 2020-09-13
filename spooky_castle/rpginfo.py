class RPGInfo():

    author = "Miles Armitage"

    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print("Welcome to " + self.title)
        print("--------------------")

    @staticmethod
    def info():
        print("Made using OOP RPG game creator [*Brezzy Bazzer*]")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
