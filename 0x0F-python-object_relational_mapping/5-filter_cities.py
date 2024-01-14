#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dbConnect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    dbCursor = dbConnect.cursor()
    dbCursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = dbCursor.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    dbCursor.close()
    dbConnect.close()
