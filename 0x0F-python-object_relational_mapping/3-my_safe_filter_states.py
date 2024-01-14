#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dbConnect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    dbCursor = dbConnect.cursor()
    match = sys.argv[4]
    dbCursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = dbCursor.fetchall()
    for row in rows:
        print(row)
    dbCursor.close()
    dbConnect.close()
