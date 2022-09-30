import http

import flask
import json
from flask import request

from .ship import Game, Ship

app = flask.Flask(__name__)


@app.route("/battleship", methods=["POST"])
def create_battleship_game():
    Game.start_game()
    ships = request.get_json()["ships"]
    for ship in ships:
        Ship(ship["x"], ship["y"], ship["size"], ship["direction"])
    return flask.jsonify({}), http.HTTPStatus.OK


@app.route("/battleship", methods=["PUT"])
def shot():
    shot = request.get_json()
    game = Game.get_game()
    res = game.shoot(shot["x"], shot["y"])

    return flask.jsonify({"result": res}), http.HTTPStatus.OK


@app.route("/battleship", methods=["DELETE"])
def delete_battleship_game():
    Game.end_game()
    return flask.jsonify({}), http.HTTPStatus.OK
