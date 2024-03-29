#!/usr/bin/python3
"""script that lists all states with n from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db_connection = MySQLdb.connect(
        host='localhost', port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db_connection.cursor()
    cur.execute("""SELECT * FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
