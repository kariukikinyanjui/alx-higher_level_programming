#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states of hbtn_0e_0_usa where
name matches the argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            )
    cursor = db.cursor()
    state_name = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (state_name, ))
    rows = cursor.fetchall()
    for row in rows:
        print(rows)
    cursor.close()
    db.close()
