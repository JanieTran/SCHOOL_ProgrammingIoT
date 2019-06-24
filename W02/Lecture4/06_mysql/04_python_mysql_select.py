import MySQLdb

# Change to appropriate username, password and database.
connection = MySQLdb.connect("localhost", "pi", "abc123", "temps")

with connection.cursor() as cursor:
    # Read from database.
    cursor.execute("SELECT tdate, ttime, zone, temperature FROM tempdat")
    # OR
    # cursor.execute("SELECT * FROM tempdat")

    print("{:15} {:15} {:15} {:15}".
        format("Date", "Time", "Zone", "Temperature"))
    print("===========================================================")

    for reading in cursor.fetchall():
        print("{:15} {:15} {:15} {:15}".
            format(str(reading[0]), str(reading[1]), str(reading[2]), str(reading[3])))

connection.close()
