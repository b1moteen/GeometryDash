from Tiles import *
from sprites import *


def load_level(filename):
    with open("maps/" + filename) as file:
        level = list(map(str.strip, file))
        max_len = len(max(level, key=len))
        level = list(map(lambda line: list(line.ljust(max_len, ".")), level))
        return level


def create_level(filename):
    level = load_level(filename)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ".":
                Tile("background", x, y)
            if level[y][x] == "#":
                Tile("box", x, y)
            elif level[y][x] == "@":
                level[y][x] = "."
                Tile("background", x, y)
                player = Player(level, x, y)
            elif level[y][x] == "-":
                Tile("floor", x, y)
            elif level[y][x] == "+":
                level[y][x] = "."
                Tile("background", x, y)
                level[y][x] = "+"
                Tile("spike", x, y)

    return player
