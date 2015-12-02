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

from serial import Serial
from time import time
from pymongo import MongoClient

serial_port = Serial('/dev/ttyUSB1', 19200, timeout=1)
sensors_module_cmds = {'temperature': ord('t'), 'humidity': ord('h'), 'luminosity': ord('l')}

def device_scheduler():
    mongo_db = MongoClient().sensors
    while(True):
        sensor_value = read_sensor(sensors_module_cmds['temperature'])
        mongo_db.temperature.insert_one(
                {
                    'timestamp': int(time()),
                    'degree': sensor_value
                }
        )

        sensor_value = read_sensor(sensors_module_cmds['humidity'])
        mongo_db.humidity.insert_one(
                {
                    'timestamp': int(time()),
                    'percent': sensor_value
                }
        )

        sensor_value = read_sensor(sensors_module_cmds['luminosity'])
        mongo_db.luminosity.insert_one(
                {
                    'timestamp': int(time()),
                    'intensity': sensor_value
                }
        )

def read_sensor(sensors_module_command):
    # for some reason, the data to write must be an iterable object
    serial_port.write([sensor_command])
    return int(serial_port.readline())
