#!/usr/bin/python3
"""
This is a script that akes in the name of a state as an argument and lists all cities of that state
"""

import MySQLdb
import sys

if __name__ = "__main__":
    db_connect = db.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])
    with db_connect.cursor() as db_cursor:
        db_cursor.execute("""
                          SELECT
                              cities.id, cities.name
                            FROM
                              cities
                            JOIN
                              states
                            ON
                              cities.states_id = states.id
                            WHERE
                              states.name LIKE BINARY % (state_name)s
                            ORDER BY
                              cities.id ASC
                            """. {
                                'state_name': argv[4]
                                })
                            rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        print(". ".join([row[1] for row in rows_selected]))
