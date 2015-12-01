#!/usr/bin/env python3

# Sensors Monitoring API

# Copyright (C) 2015  Augusto Lopez Dantas aldantas@protonmail.com
# Copyright (C) 2015  Gabriel Putrick gputrick@gmail.com

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from flask import Flask, jsonify, Response, json
from flask.ext.pymongo import PyMongo
from flask.ext.cors import CORS
from multiprocessing import Process
from filters import filter_by_timestamp
from hello import hello

# CONFIGURATION
app = Flask('sensors')
CORS(app)
mongo = PyMongo(app)
route_prefix = '/sensors/api/'

@app.route(route_prefix + 'temperature/<int:timestamp>')
def temperature(timestamp):
    temperature_list = filter_by_timestamp(mongo.db.temperature, timestamp)
    return Response(json.dumps(temperature_list), mimetype='application/json')

@app.route(route_prefix + '/humidity/<int:timestamp>')
def humidity(timestamp):
    humidity_list = filter_by_timestamp(mongo.db.humidity, timestamp)
    return Response(json.dumps(humidity_list), mimetype='application/json')

@app.route(route_prefix + '/luminosity/<int:timestamp>')
def luminosity(timestamp):
    luminosity_list = filter_by_timestamp(mongo.db.luminosity, timestamp)
    return Response(json.dumps(luminosity_list), mimetype='application/json')

if __name__ == "__main__":
    api = Process(target=hello)
    api.start()
    app.run(host='0.0.0.0')
