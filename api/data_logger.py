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

serial_port = Serial('/dev/ttyUSB0', 19200, timeout=1)
sensors_module_cmds = {'temperature': ord('t'), 'humidity': ord('h'), 'luminosity': ord('l')}
separation_char = "*"

def device_scheduler():
    MongoClient().drop_database('sensors_monitor')
    mongo_db = MongoClient().sensors_monitor
    while(True):
        temperature, humidity, luminosity = read_sensors()
        timestamp = int(time()) * 1000;

        mongo_db.temperature.insert_one(
                {
                    'timestamp': timestamp,
                    'degree': int(temperature)
                }
        )

        mongo_db.humidity.insert_one(
                {
                    'timestamp': timestamp,
                    'percent': int(humidity)
                }
        )

        mongo_db.luminosity.insert_one(
                {
                    'timestamp': timestamp,
                    'intensity': int(luminosity)
                }
        )

def read_sensor(sensors_module_command):
    # must be an iterable object
    serial_port.write([sensors_module_command])
    sensor_value = serial_port.readline().rstrip(separation_char)
    if sensor_value.isnumeric:
        return int(sensor_value)
    else:
        return ''

def read_sensors():
    serial_port.write([ord('t'), ord('h'), ord('l')])
    return serial_port.readline().decode().rstrip(separation_char).split(separation_char)
