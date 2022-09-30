import unittest
from battleship.ship import Ship, Game, ShipExistError, Result, Item, Direction


class AddShipTestCase(unittest.TestCase):
    def test_add_horizontal_ship(self):
        Game.start_game()
        s = Ship(2, 1, 4, "H")
        expected_game_coordinates = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, s, s, s, s, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        game = Game.get_game()
        game_coordinates = game.coordinates

        for y in range(len(game_coordinates)):
            for x in range(len(game_coordinates[y])):
                self.assertEqual(
                    game_coordinates[y][x], expected_game_coordinates[y][x]
                )

    def test_add_vertical_ship(self):
        Game.start_game()
        s = Ship(2, 1, 5, Direction.VERTICAL)
        expected_game_coordinates = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, s, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, s, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, s, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, s, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, s, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        game = Game.get_game()
        game_coordinates = game.coordinates

        for y in range(len(game_coordinates)):
            for x in range(len(game_coordinates[y])):
                self.assertEqual(
                    game_coordinates[y][x], expected_game_coordinates[y][x]
                )

    def test_add_vertical_and_horizontal_ship(self):
        Game.start_game()
        s = Ship(2, 1, 4, Direction.HORIZONTAL)
        t = Ship(7, 4, 3, Direction.VERTICAL)
        expected_game_coordinates = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, s, s, s, s, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        game = Game.get_game()
        game_coordinates = game.coordinates

        for y in range(len(game_coordinates)):
            for x in range(len(game_coordinates[y])):
                self.assertEqual(
                    game_coordinates[y][x], expected_game_coordinates[y][x]
                )

    def test_two_overlapping_ship(self):
        Game.start_game()
        s = Ship(2, 1, 4, "H")

        def func():
            t = Ship(4, 0, 5, "V")

        self.assertRaises(ShipExistError, func)


class ShootingTestCase(unittest.TestCase):
    def setUp(self):
        Game.start_game()
        self.s = Ship(2, 1, 4, Direction.HORIZONTAL)
        self.t = Ship(7, 4, 3, Direction.VERTICAL)

    def test_shoot_ship_water(self):
        game = Game.get_game()
        result = game.shoot(3, 5)
        game_coordinates = game.coordinates
        self.assertEqual(result, Result.WATER)
        s = self.s
        t = self.t
        expected_game_coordinates = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, s, s, s, s, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        for y in range(len(game_coordinates)):
            for x in range(len(game_coordinates[y])):
                self.assertEqual(
                    game_coordinates[y][x], expected_game_coordinates[y][x]
                )

    def test_shoot_vertical_ship(self):
        game = Game.get_game()
        result = game.shoot(7, 5)
        game_coordinates = game.coordinates
        self.assertEqual(result, Result.HIT)
        s = self.s
        t = self.t
        expected_game_coordinates = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, s, s, s, s, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        for y in range(len(game_coordinates)):
            for x in range(len(game_coordinates[y])):
                self.assertEqual(
                    game_coordinates[y][x], expected_game_coordinates[y][x]
                )

        def test_shoot_horizontal_ship(self):
            game = Game.get_game()
            result1 = game.shoot(2, 1)
            result2 = game.shoot(3, 1)
            result3 = game.shoot(4, 1)
            result4 = game.shoot(5, 1)
            result5 = game.shoot(6, 1)
            result6 = game.shoot(4, 1)
            game_coordinates = game.coordinates
            self.assertEqual(result1, Result.HIT)
            self.assertEqual(result2, Result.HIT)
            self.assertEqual(result3, Result.HIT)
            self.assertEqual(result4, Result.SINK)
            self.assertEqual(result5, Result.WATER)
            self.assertEqual(result6, Result.HIT)
            s = self.s
            t = self.t
            expected_game_coordinates = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, s, s, s, s, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, t, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
            for y in range(len(game_coordinates)):
                for x in range(len(game_coordinates[y])):
                    self.assertEqual(
                        game_coordinates[y][x], expected_game_coordinates[y][x]
                    )


if __name__ == "__main__":
    unittest.main()
