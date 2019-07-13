#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-12 09:36
# @Author  : bingo
# @Site    : 
# @File    : geohash.py
# @Software: PyCharm

"""
给数据库的表proposal更新geohash字段
"""
"""A simple GeoHash implementation."""

# Forward and reverse base 32 map
BASESEQUENCE = '0123456789bcdefghjkmnpqrstuvwxyz'
BASE32MAP = dict((k, count) for count, k in enumerate(BASESEQUENCE))
BASE32MAPR = dict((count, k) for count, k in enumerate(BASESEQUENCE))


def _float_to_bits(value, lower=-90.0, middle=0.0, upper=90.0, length=15):
    """Convert a float to a list of GeoHash bits."""
    ret = []
    for i in range(length):
        if value >= middle:
            lower = middle
            ret.append(1)
        else:
            upper = middle
            ret.append(0)
        middle = (upper + lower) / 2
    return ret


def _bits_to_geohash(value):
    """Convert a list of GeoHash bits to a GeoHash."""
    ret = []
    # Get 5 bits at a time
    for i in (value[i:i + 5] for i in range(0, len(value), 5)):
        # Convert binary to integer
        # Note: reverse here, the slice above doesn't work quite right in reverse.
        total = sum([(bit * 2 ** count) for count, bit in enumerate(i[::-1])])
        ret.append(BASE32MAPR[total])
    # Join the string and return
    return "".join(ret)


def encode(lonlat, length=12):
    """Encode a (lon,lat) pair to a GeoHash."""
    assert len(lonlat) == 2, "Invalid lon/lat: %s" % lonlat
    # Half the length for each component.
    length /= 2
    lon = _float_to_bits(lonlat[0], lower=-180.0, upper=180.0, length=int(length * 5))
    lat = _float_to_bits(lonlat[1], lower=-90.0, upper=90.0, length=int(length * 5))
    # Zip the GeoHash bits.
    ret = []
    for a, b in zip(lon, lat):
        ret.append(a)
        ret.append(b)
    return _bits_to_geohash(ret)


import pymysql


def db():
    connection = pymysql.connect(
        host='',
        port=3306,
        user='root',
        password='',
        db='',
        charset='utf8'
    )

    # 获取游标
    cursor = connection.cursor()

    # 更新geohash字段的sql
    # sql = f'UPDATE `proposal` SET `geohash`={encode(`coordinate`)}'
    sql_select = 'SELECT `id`, `coordinate` FROM `proposal`'
    sql_update = 'UPDATE `proposal` SET `geohash`=%s WHERE `id`=%s'
    try:
        cursor.execute(sql_select)
        result = cursor.fetchall()
        # print(result)
        for row in result:
            table_id, coordinate = row[0], row[1].split(',')
            coordinate = list(map(float, coordinate))
            geohash = encode(coordinate)
            print(table_id, coordinate, geohash)
            try:
                # pass
                cursor.execute(sql_update, args=(geohash, int(table_id)))
            except Exception:
                print('update failed')
                raise ('update failed')
    except Exception as e:
        connection.rollback()
    finally:
        connection.close()


if __name__ == "__main__":
    db()
