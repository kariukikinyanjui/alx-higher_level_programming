#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""
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
    query = "SELECT cities.name FROM cities INNER JOIN\
            states ON states.id=cities.state_id WHERE states.name=%s"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    # Extract city names from the rows
    city_names = list(row[0] for row in rows)

    # Print the city names separated by commas
    print(*city_names, sep=", ")

    cursor.close()
    db.close()
