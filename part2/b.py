#!/usr/bin/env python
import this
import random
from flask import Flask
from flask_restful import Api, Resource
from gevent.pywsgi import WSGIServer
import logging
import logging.config

logging.config.dictConfig({"version": 1, "root": {"level": "INFO"}})

s = "".join([this.d.get(c, c) for c in this.s])
the_zen_of_python = [rule for rule in s.split('\n') if rule and "The Zen of Python, by Tim Peters" not in rule]

max_idx = len(the_zen_of_python) - 1

app = Flask(__name__)
api = Api(app)


class TheZenOfPython(Resource):
    def get(self):
        idx = random.randint(0, max_idx)
        return the_zen_of_python[idx]


# Add route
api.add_resource(TheZenOfPython, "/")


def run_wsgi():
    host = "0.0.0.0"
    port = 1234
    http = WSGIServer((host, port), app.wsgi_app)
    logging.info("Listen on: http://{host}:{port}/".format(host=host, port=port))
    http.serve_forever()


if __name__ == '__main__':
    run_wsgi()
