#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-09 16:11
# @Author  : bingo
# @Site    : 
# @File    : 2.py
# @Software: PyCharm

"""
第 0002 题**：将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。
"""

import pymysql

# 0001生成的激活码
codes = ['fqhWaCoV0bqtNSd9Y5Ar', 'xSOfRwEUunYoABKEEXQd', 'FeTFEPbc5xhDdAnu3Wte', 'u7oL8JxQkOZDZfUXkJ6q', 'h60BP3MXGOyyhthuFkr7', '11R6EdMlrY3dtYiwcdcm', 'BCKgAMtr9t54YSorumk1', 'V5jlfBJuCB66EwxNTZFl', 'Z8QWvMeR2LNZTACNByCE', 'gldnrkPQCtVljz9yp2se', 'YF0Xps44U5ny4Uh1enbO', 'tcuFiAJBeISW0UpGmwsF', 'ga7v8Y89pcTL9kq48GbV', 'e910ebn2HfQAjWJiFqCL', 'fZ3W1jTHOYwtCdjrtk3g', 'FA71xXI78epIefo3gYGY', 'U0HsLvFlNbON7V1DMmQT', 'URWWzgZEGuii3w2DtvYt', 'IHB7pzyF9Phyo1uWVs8j', 'ksM6gqOPmqhBWzE0vkwF', '7iYgbgBVOxvj9QFTNmjN', 'VYOmsLcV8OGOMzgwdom9', 'Fvyg2uExu4zEeWhnidDI', 'eUyfEi0nZstom2yot8CZ', 'OWf5PxHbEIF8yu6g6K5i', '10jEH5XzBJOEaopo21ny', 'zentBVupg2qm6hSLJFoj', 'Yks7vi8o1LlsvfDkRjqf', 'iEGrJo8TI9uSR3BdrRMj', 'G56C5p8ZlPqVvO3uzcya', 'IuGQSydeEDKj5MLMsDkt', 'fuv0HoqI2Tfq0OMVrTNU', 'Kat9nV1Tf9pIiolSXcnv', 'rgHYPogllvsXYkk1HnxH', 'TF34bu2llPeADXtpVgi7', 'Cbx5wuNAEwBp6OyCR2u7', 'hCnOlXoIM3rgy7hQKeuK', 'qF0UwD12OX4HMlYslpy0', 'EivsnXlqcENY7VO2GRiZ', 'R2eYp1QxuJqa0FehfBX8', 'h8GDSyQ9PGLdWyUyTpkQ', 'Yt5nTjVXmIzlJWkOpmEK', 'Zt0awBkKIfnECZdYw9XK', 'zpIdjKrhwuB2nycHCN5Y', 'EAlVYDLJKlz9uXS34Q10', 'Jo2HUC6sdJgyKLMvUW4P', '9J2TaY3zXFGULDWVcAuq', 'ioSdrRt6BurptZnuIsYv', 'U0tfbCqdICIH6DAfESum', '3zhwLbXvGyfnnL5eRGkj', 'sBX677c5x8OSQQjRpccm', 'jNoZbFXiFeOPJ6uHpiMn', 'B5GKbyDbnXOpJ9Z3Ca0I', 'dwGr7KVob6477mSUu5QW', 'aHgispcL0uioxgAqzzyR', 'NiHZl6EFS357JH01Lqnt', 'IMXTL4wRqrNhsngse5jl', '84wqsHDhIZxOoB8eqVVX', '4FXFsZwZ3jmxrmVe9wjY', '84v0FrEgXyOa0xabn1Bl', 'klu5rT4XCNR7xtZyHata', '1EXeQJRJVc5RgGwzq9ig', 'Azrrs8AbSO5AksjRjW9m', 'qbQybq2soVhJQhENE4UL', 'wJJ45EJ36xrcn0albplA', '8UmjTC35tjAAzObczdnQ', 'C3OR75H1AXPTNRJLnZwh', 'tT3Stt3bvt5768wQaviH', 'CKCTUGDZifQXjf0VZdWp', 'VOOXxL58mJZZ2e9FKzxO', 'cXAAi1gjvNu6SDSmE3XS', 'mNfONuWf3bw2dAwImCnb', 'goG34eEcQF6Yy8GGzCc4', 'lnLP3EPKhMkLDlFxPjq8', 'BPkSpfPkA1wIHhGvEKt4', 'hFoZshjCnrSEtesSHUkS', 'LR1vnok6ES3LNOh8DkCY', 'cd0vvBwOQr0Wwe0ue7lv', '7NXnYXlGc5tjU4UsH6IK', 'q1LuzBSIPevkyuDNpTI5', 'CqKReb9vZ92gXVSqeNud', '2r7U17xTLF87t41drOmC', 'vHZygrOR3VSaycjlW2ew', '0GQr9Ml4FjBmQhMa5oHX', '3sxPKH4LnsX6zsEWJcrs', 'bwxn7vm0XCFG73bCL9Qf', 'vemyoYyLgqpkyZdUTuEx', 'YNfuaweVBf9qMgum7DBh', '4ruTT0ZSImvvybCooIiY', 'nSOTK74A5wE28KsjQy7j', 'XXV7OWPd1Dy0G06Uus3f', 'TWHu7gHWBaWWDaIcV3XV', '2yXbBkScRIDjcSVZUCdC', 'Nr6LTfg2JA26iSQ1BpQ1', 'vy9ilTxEKz6XO4Pj3IUu', 'UaCCs2aURInEnjHZuu07', 'R5FIhiPrvvBGyBKs8MQt', 'Zjqi9mxD1BsiZBxItILe', 'TCZxM2FRIOwMfXv7l6mI', 'fJjIq3PzJUQiJMw3rWnt', 'oqTxbonlcmw53MiMqZXB', 'NRV1zladxZIZvftdbD0q', '7DOY4S28sK3cLxDwvYgj', 'X6pMDGQCP22d0NF0JFLB', 'o0hKio0k6Tr5VGCW9JfD', '6NDwvIoEQb7GEI1dhUkl', 'uP5gLMbLkcGSpBABnAJz', 'aZsG2NsauGE8y87tOLrv', 'oJBAo1meEzhDp7PpVDD5', 'BQab5B0iXh8DMLkFrkG6', 'sDWxJ5081EyocKZgvIW4', '9KHcEE3O4aL9I8lrxIj5', 'ypE9HwTLgHw9YFBPpvuA', 'MUgQgLyGIopu8RjoQ4vC', 'ooTRw2DlJRm0sua3huBS', 'GeoFgSXI251XxYH3XaH5', 'KKAiE4fRuJPcLmR2xeVE', '03OJ3ABeiIkhFMWg4Jov', '7NCD8X2DXOtPrvgTA8N6', '8L2UDNfd7oZKse2grk24', 'WBfYMUG49TwF4X4J9qEF', 'uQrFVl5eBL1AZjmJ3Ikz', 'ix8VEbNe5sx0l9n8w04t', 'gzdjm2m6AZBA8gizhHGU', '2hvsIpMTonoLD0ZWeujR', '2rVbH4sJrVNjl5pfPqaC', '7rngMNOaGbJCji79ezLR', 'oJE3afvedaZOmGLMaibi', 'ZTovhR9LVN7xzsq6fjQo', 'sADDRO5LJMfgkUFFEyQg', 'V9J4HjJeRU8PmAppARgN', 'mG97mLxKhUYEv6BU170M', 'xOgfPDzmzn85UW6qX9kD', 'evpxoFrWkJOr4RoJfg1g', '8mFkI0OaOfUb1KjVZAEi', 'Gf6vTyvARybfWQ7w0LYm', 'ufQpAIBW3TdPw2PBZIgv', 'W0RZddWp737zM2l3BsAR', 'fjF56vsOAfrw2SwaRqTX', 'Wc8hKpcCu5HtvZuVDESz', 'Q0LGPFiR4qDWC2pquwkt', '7WH7vAmaYIWLcswwjRmp', 'd9opGDFfXR0AMOwpHJ48', 'ahiHEfD8zBRe5xBex5bk', '3mCcR6mfaRwQFEkfbcer', 'OFPuMroYbRRillYqLZUz', '0LKbC3thOJzHbfp8aoz2', 'TJC5McwOKuYrXiphjwYo', '4qo0pdNCePDquExIep58', 'KqhTbwdGKvvgKcDdAJWZ', 'ayz6rlOnrQF2UkuGVa6W', 'h02mAf9ScmSFf9Oz2EjI', 'PGBRAnSOqCCleRsgaFUk', '4SJeOZhHPj75MuNirNcV', 'UlUIiRomF5JW6V7H7z80', 'pKoZzOGBkmztTqtx9BmB', 'SLjTSkZVRw1fza1zqYdv', 'NdqQBAluMD9NPe5Pg5gs', 'oRonvqYgQf0892iU0ShM', '6LX6vEviVSP4jYNltDu8', 'VM65Zp2Wy3FgxP6tXDxg', 'yFoCi1upD38YBnf0NtOO', '1ghrlscBSKnlESoJLoEY', 'Y6km1Oo4KXxH8rki4lXd', 'HNHfQZOLmj6sn1xkgesd', 'r61nXrjD7MSbTun5W9E6', '09Jiw69cb44mIPMHOiPK', 'xfvbVmqTAJzb23Fr7bNz', '8ZBLOxB6s9oSiS1GDXN1', 'f7DG3Lj6s35i0Z7fe2p0', 'VSQixfu6FA5mO8MNAMP4', 'yghwwdWNdUvHnAl0tiAM', 'PdcrCo9zK5V3N0HX5Hs4', 'xas0K0jsplFClozlhp5C', 'AG6YIGMMd1I157wuEpQn', 'w87hK1sy2Wqcfs8xSLfM', '2Kj0KRPPQJwAza70oJ9C', 'plEhPZ3u9QF2X0rVm8go', 'CgfZfmyDOlz1UX1SHsmW', 'k646z8XUbKAc6EYusPit', 'c8VP3z4OIMFY3TLpCGss', 'lhseKvItgC4eimFhLjcz', 'kka62MFiMFn8dl0N0o8A', 'vIf4SuHYImbO6mV5VJzk', 'azeyZSQUkNYfkXedLEBL', 'sp8wAzLO6OSQQ6RHCB1t', 'apmb8BJaCuw3027cplbg', 'CLRie5egYbhq76DRUG3p', '7sciV6ZzJjuCy8wbxHAm', 'yX28HIOzESStTLKiGXc0', 'sjLvXcuhjDaWWFViRQV8', '898TIIBMjTd0wxX8l5G2', 'UrM6pU58awLVnZmpiEkt', 'o7U4pIPDn0iShBWh6ZMr', 'cdrNY2pBg5NjHWzICH98', 'bY8oFVh5DI3oENDr60uC', 'Y2WoooHYOd9Hry1yXFOa', 'I6J2Au7hYMRysvRjXFEX', 'J5qivVLbNhg20VVnUEZx', 'xSjl7dn4bX4EBg5tUXDL']


connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='mingyue6868',
                             db='activation_code',
                             charset='utf8')

# 获取游标
cursor = connection.cursor()

# 如果不存在表，则创建表
table = cursor.execute('''
CREATE TABLE IF NOT EXISTS `codes` (
    `id` INT AUTO_INCREMENT,
    `code` VARCHAR(30) UNIQUE,
    PRIMARY KEY(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
''')

# 插入数据
insert = cursor.executemany('''
INSERT INTO `codes` (code) VALUES (%s) 
''', codes)

# 提交
connection.commit()