from werkzeug.exceptions import HTTPException


class InvalidDirectionException(HTTPException):
    code = 400
    description = "No Direction here"


class ShipExistError(HTTPException):
    code = 400
    description = "Position already occupied"


class NoGameError(HTTPException):
    code = 400
    description = "No Game Started"


class PositionError(HTTPException):
    code = 400
    description = "No Ship in this Position"


class Result:
    HIT = "HIT"
    WATER = "WATER"
    SINK = "SINK"


class Item:
    WATER = 0
    HIT = 2


class Direction:
    VERTICAL = "V"
    HORIZONTAL = "H"


class Ship:
    def __init__(self, x, y, size, direction):
        self.size = size
        self.hit = 0
        self.x = x
        self.y = y
        self.direction = direction
        self.game = Game.get_game()
        self.game.add_ship(self)

    def shot(self):
        self.hit += 1
        return self.hit == self.size

    def get_coordinate(self):
        for index in range(self.size):
            if self.direction == Direction.VERTICAL:
                yield self.y + index, self.x,
            elif self.direction == Direction.HORIZONTAL:
                yield self.y, self.x + index
            else:
                raise InvalidDirectionException()


class Game:
    game = None

    def __init__(self, x=10, y=10):
        self.coordinates = [[0 for index in range(x)] for index in range(y)]

    def add_ship(self, ship):
        try:
            for y, x in ship.get_coordinate():
                if self.coordinates[y][x] == 0:
                    self.coordinates[y][x] = ship
                else:
                    raise ShipExistError()
        except IndexError:
            raise PositionError()

    @classmethod
    def start_game(cls):
        cls.game = Game()

    @classmethod
    def end_game(cls):
        cls.game = None

    @classmethod
    def get_game(cls):
        if not cls.game:
            raise NoGameError()
        return cls.game

    def shoot(self, x, y):
        try:
            position = self.coordinates[y][x]
        except IndexError:
            raise PositionError()
        if position == Item.WATER:
            return Result.WATER
        elif position == Item.HIT:
            return Result.HIT
        else:
            sunk = position.shot()
            self.coordinates[y][x] = Item.HIT
            return Result.SINK if sunk else Result.HIT
