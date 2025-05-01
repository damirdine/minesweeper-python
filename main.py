from typing import override


class Film:
    def __init__(self, name):
        self.name = name

    def go(self):
        print("Hello Film")


class FilmCassette(Film):

    @override
    def go(self):
        print("Hello Cassette")


cassette = FilmCassette("Popop")
cassette.go()
