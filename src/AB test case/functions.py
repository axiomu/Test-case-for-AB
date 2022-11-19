# -*- coding: utf-8 -*-
'''
Created on Sat Nov 19 20:35:01 2022

@author: Igor
'''

import sqlite3



# DB creation =============================================================================


con = sqlite3.connect('AB_test_DB.db')

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS user_dictionary(user_id INTEGER PRIMARY KEY,\
            last_name TEXT, first_name TEXT, email TEXT UNIQUE, phone_number TEXT UNIQUE)')

cur.execute("""
    INSERT INTO user_dictionary VALUES
       (1,	'Manizha',	'Sangin',	'test1@gmail.com', '+992921234567'),
       (2,	'Ivanov',	'Ivan',	'test2@gmail.com', '+992921231234'),
       (3,	'Schwarzenegger',	'Arnold',	'test3@gmail.com',	'+992921231212')

""")
con.commit()


cur.execute('CREATE TABLE IF NOT EXISTS bookings(booking_id INTEGER PRIMARY KEY,\
            room_id INTEGER, start_datetime DATETIME, end_datetime DATETIME, user_id INTEGER)')

cur.execute("""
    INSERT INTO bookings VALUES
       (1, 3, '2022-11-22 14:00:00',    '2022-11-22 15:00:00', 1),
       (2, 3, '2022-11-22 16:00:00',    '2022-11-22 18:00:00', 1),
       (3, 4, '2022-11-23 12:00:00',    '2022-11-23 14:00:00', 3),
       (4, 5, '2022-11-22 14:00:00',    '2022-11-22 15:00:00', 2)

""")
con.commit()

con.close()


# =============================================================================


