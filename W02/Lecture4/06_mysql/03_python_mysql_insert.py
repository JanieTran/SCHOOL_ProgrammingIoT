# Reference: http://raspberrywebserver.com/sql-databases/using-mysql-on-a-raspberry-pi.html
# See: https://dev.mysql.com/doc/refman/5.5/en/sql-syntax.html
import MySQLdb

# Change to appropriate username, password and database.
connection = MySQLdb.connect("localhost", "pi", "abc123", "temps")

with connection.cursor() as cursor:
    # Note use of triple quotes for formatting purposes.
    # You can use one set of double quotes if you put the whole string on one line.
    cursor.execute("""INSERT INTO tempdat
        VALUES(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'kitchen', 21.7)""")
    cursor.execute("""INSERT INTO tempdat
        VALUES(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'greenhouse', 24.5)""")
    cursor.execute("""INSERT INTO tempdat
        VALUES(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'garage', 18.1)""")

    cursor.execute("INSERT INTO tempdat VALUES(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'kitchen', 20.6)")
    cursor.execute("INSERT INTO tempdat VALUES(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'greenhouse', 17.1)")
    cursor.execute("INSERT INTO tempdat VALUES(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'garage', 16.2)")

    cursor.execute("INSERT INTO tempdat VALUES(CURRENT_DATE(), NOW(), 'kitchen', 22.9)")
    cursor.execute("INSERT INTO tempdat VALUES(CURRENT_DATE(), NOW(), 'greenhouse', 25.7)")
    cursor.execute("INSERT INTO tempdat VALUES(CURRENT_DATE(), NOW(), 'garage', 18.2)")

connection.commit()
connection.close()

print("Data committed.")
