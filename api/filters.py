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

def filter_by_timestamp(collection, timestamp):
    values_list = []
    for value in collection.find({'timestamp': {'$gt': timestamp}}):
        del(value['_id'])
        values_list.append(value)
    return values_list
